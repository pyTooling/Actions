[CmdletBinding()]
Param(
# Clean up all files and directories
  [switch]$clean,

# Commands
  [switch]$all,
  [switch]$alldoc,
  [switch]$copyall,

  [switch]$doc,
  [switch]$livedoc,
  [switch]$html,
  [switch]$latex,
  [switch]$pdf,
  [switch]$doccov,

  [switch]$unit,
  [switch]$liveunit,
  [switch]$copyunit,

  [switch]$cov,
  [switch]$livecov,
  [switch]$copycov,

  [switch]$type,
  [switch]$livetype,
  [switch]$copytype,

  [switch]$nooutput,

  [switch]$build,
  [switch]$install,

# Display this help"
  [switch]$help
)

$ProjectName =    "Actions"
$PackageName =    "myPackage"
$PackageVersion = "7.5.1"
$PythonVersion =  "3.14"
$LaTeXDocument =  "${ProjectName}.tex"

# set default values
$EnableDebug =   [bool]$PSCmdlet.MyInvocation.BoundParameters["Debug"]
$EnableVerbose = [bool]$PSCmdlet.MyInvocation.BoundParameters["Verbose"] -or $EnableDebug

# Display help if no command was selected
$help = $help -or ( -not (
  $all -or $alldoc -or $copyall -or
    $clean -or
    $doc -or $livedoc -or $doccov -or $html -or $latex -or $pdf -or
    $unit -or $liveunit -or $copyunit -or
    $cov -or $livecov -or $copycov -or
    $type -or $livetype -or $copytype -or
    $build -or $install
  )
)

Write-Host "================================================================================" -ForegroundColor Magenta
Write-Host "$ProjectName Documentation Compilation and Assembly Tool"                         -ForegroundColor Magenta
Write-Host "================================================================================" -ForegroundColor Magenta

if ($help) {
  Get-Help $MYINVOCATION.MyCommand.Path -Detailed
  exit 0
}

if ($all) {
  $doc =      $true
  $html =     $true
  $latex =    $true
  $pdf =      $true
  $unit =     $false
  $copyunit = $false
  $cov =      $true
  $copycov =  $false
  $type =     $true
  $copytype = $true
} elseif ($alldoc) {
  $doc =      $true
  $html =     $true
  $latex =    $true
  $pdf =      $true
}

if ($livecov -or $liveunit) {
  $cov = $unit = $false
}
if ($livecov -or $cov) {
  $liveunit = $unit = $false
}

if (($doc -or $alldoc -or $livedoc) -and -not ($html -or $latex -or $pdf)) {
  $html = $true
}

if ($copyall) {
  $copyunit = $false
  $copycov =  $false
  $copytype = $true
}

if ($clean) {
  Write-Host -ForegroundColor DarkYellow    "[live][DOC]       Cleaning documentation directories ..."
  Remove-Item -Recurse -Force .\doc\_build\*          -ErrorAction SilentlyContinue
  Remove-Item -Recurse -Force .\doc\$PackageName\*    -ErrorAction SilentlyContinue

  Write-Host -ForegroundColor DarkYellow    "[live][BUILD]     Cleaning build directories ..."
  Remove-Item -Recurse -Force .\build\bdist.win-amd64 -ErrorAction SilentlyContinue
  Remove-Item -Recurse -Force .\build\lib             -ErrorAction SilentlyContinue
}

if ($build) {
  Write-Host -ForegroundColor Yellow        "[live][BUILD]      Cleaning build directories ..."
  Remove-Item -Recurse -Force .\build\bdist.win-amd64 -ErrorAction SilentlyContinue
  Remove-Item -Recurse -Force .\build\lib             -ErrorAction SilentlyContinue

  Write-Host -ForegroundColor Yellow        "[live][BUILD]      Building $PackageName package as wheel ..."
  py -$PythonVersion -m build --wheel --no-isolation

  Write-Host -ForegroundColor Yellow        "[live][BUILD]      Building wheel finished"
}
if ($install) {
  if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")) {
    Write-Host -ForegroundColor Yellow      "[live][INSTALL]    Installing $PackageName with administrator rights ..."
    $proc = Start-Process pwsh.exe "-NoProfile -ExecutionPolicy Bypass -WorkingDirectory `"$PSScriptRoot`" -File `"$PSCommandPath`" `"-install`"" -Verb RunAs -Wait

    #    Write-Host -ForegroundColor Yellow   "[live][INSTALL]    Wait on administrator console ..."
    #    Wait-Process -Id $proc.Id
  } else {
    Write-Host -ForegroundColor Cyan        "[ADMIN][UNINSTALL] Uninstalling $PackageName ..."
    py -$PythonVersion -m pip uninstall -y $PackageName
    Write-Host -ForegroundColor Cyan        "[ADMIN][INSTALL]   Installing $PackageName from wheel ..."
    py -$PythonVersion -m pip install .\dist\$PackageName-$PackageVersion-py3-none-any.whl

    Write-Host -ForegroundColor Cyan        "[ADMIN][INSTALL]   Closing window in 5 seconds ..."
    Start-Sleep -Seconds 5
  }
}

$runUnitCopyFunc = {
  param($live)

  cp -Recurse -Force .\report\unit\html\* .\doc\_build\html\unittests
  if ($live) {
    Write-Host -ForegroundColor DarkBlue      "[live][UNIT]      Copyed unit testing report to 'unittests' directory in HTML directory"
  }
}
$runUnitFunc = {
  param($live, $copy, $runCopyStr)

  $runCopyFunc = [ScriptBlock]::Create($runCopyStr)

  $env:PYTHONPATH="."
  $env:ENVIRONMENT_NAME = "Windows (x86-64)"
  pytest -raP --color=yes --template=html1/index.html --report=report/unit/html/index.html --split-report tests/unit

  if ($copy) {
    & $runCopyFunc $live
  }
}

$runCovCopyFunc = {
  param($live)

  cp -Recurse -Force .\report\coverage\html\* .\doc\_build\html\coverage
  if ($live) {
    Write-Host -ForegroundColor DarkMagenta   "[live][COV]       Copyed code coverage report to 'coverage' directory in HTML directory"
  }
}
$runCovFunc = {
  param($live, $copy, $runCopyStr)

  $runCopyFunc = [ScriptBlock]::Create($runCopyStr)

  $env:PYTHONPATH="."
  $env:ENVIRONMENT_NAME = "Windows (x86-64)"
  coverage run --data-file=.coverage --rcfile=pyproject.toml -m pytest -ra --color=yes tests/unit

  if ($live) {
    Write-Host -ForegroundColor DarkMagenta   "[live][COV]       Convert coverage report to HTML ..."
  }
  coverage html

  if ($live) {
    Write-Host -ForegroundColor DarkMagenta   "[live][COV]       Convert coverage report to XML (Cobertura) ..."
  }
  coverage xml

  if ($live) {
    Write-Host -ForegroundColor DarkMagenta   "[live][COV]       Convert coverage report to JSON ..."
  }
  coverage json

  if ($live) {
    Write-Host -ForegroundColor DarkMagenta   "[live][COV]       Write coverage report to console ..."
  }
  coverage report

  if ($copy) {
    & $runCopyFunc $live
  }
}

$runTypingCopyFunc = {
  param($live)

  cp -Recurse -Force .\report\typing\* .\doc\_build\html\typing
  if ($live) {
    Write-Host -ForegroundColor DarkCyan    "[live][TYPE]      Copyed typing report to 'typing' directory in HTML directory."
  }
}
$runTypingFunc = {
  param($PackageName, $live, $copy, $runCopyStr)

  $runCopyFunc = [ScriptBlock]::Create($runCopyStr)

  $env:MYPY_FORCE_COLOR = 1
  mypy.exe -p $PackageName

  if ($copy) {
    & $runCopyFunc $live
  }
}

$compileHTMLDocFunc = {
  param($PyVersion, $live, $copyUnit, $copyCov, $copyType, [scriptblock]$runUnitCopyFunc, [scriptblock]$runCovCopyFunc, [scriptblock]$runTypingCopyFunc)

  Push-Location "doc"
  py -$PyVersion -m sphinx.cmd.build --builder html --write-all --doctree-dir _build/doctrees-html --jobs 8 --warning-file _build/sphinx-html-warnings.log --verbose . _build/html
  Pop-Location

  if ($copyUnit) {
    & $runUnitCopyFunc $live
  }
  if ($copyCov) {
    & $runCovCopyFunc $live
  }
  if ($copyType) {
    & $runTypingCopyFunc $live
  }
}
$compileLaTeXDocFunc = {
  param($PyVersion, $LaTeXDocument)

  Push-Location "doc"
  py -$PyVersion -m sphinx.cmd.build --builder latex --write-all --doctree-dir _build/doctrees-latex --jobs 8 --warning-file _build/sphinx-latex-warnings.log --verbose . _build/latex

  Move-Item -Force "_build/latex/doc-CC--BY_41.0-green" "_build/latex/doc-CC--BY_41_0-green.png"

  $texFile = Get-Content "_build/latex/$LaTeXDocument"
  $texFile.Replace('{{doc-CC--BY_41}.0-green}}', '{{doc-CC--BY_41_0-green}.png}}') | Set-Content "_build/latex/$LaTeXDocument"

  Pop-Location
}
$compilePDFDocFunc = {
  param($Document)

  if (Test-Path -Path "doc/_build/latex" -PathType Container) {
    Push-Location "doc/_build/latex"
    latexmk -C
    # --latexoption=--cnf-line=max_print_line=1000
    latexmk --lualatex --latexoption=--c-style-errors --interaction=nonstopmode --halt-on-error $Document
    Pop-Location
  } else {
    Write-Host -ForegroundColor Yellow "No LaTeX source directory 'doc/_build/latex' found."
  }
}

# Unit testing (with/without code coverage)
if ($livecov) {
  Write-Host -ForegroundColor DarkMagenta   "[live][COV]       Running Unit Tests using pytest with coverage ..."
  & $runCovFunc $true $copycov $runCovCopyFunc
  Write-Host -ForegroundColor DarkYellow    "[live][COV]       Unit Tests finished"
} elseif ($liveunit) {
  Write-Host -ForegroundColor DarkYellow    "[live][UNIT]      Running Unit Tests using pytest ..."
  & $runUnitFunc $true $copyunit $runUnitCopyFunc
  Write-Host -ForegroundColor DarkYellow    "[live][UNIT]      Unit Tests finished"
} elseif ($cov) {
  Write-Host -ForegroundColor DarkYellow    "[Job1][COV]       Running Unit Tests using pytest with coverage ..."
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Starting Coverage jobs ..."
  $testJob = Start-Job -Name "Coverage"  -ScriptBlock $runCovFunc -ArgumentList $false, $copycov, $runCovCopyFunc
} elseif ($unit) {
  Write-Host -ForegroundColor DarkYellow    "[Job1][UNIT]      Running Unit Tests using pytest ..."
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Starting UnitTests jobs ..."
  $testJob = Start-Job -Name "UnitTests" -ScriptBlock $runUnitFunc -ArgumentList $false, $copyunit, $runUnitCopyFunc
}

# Static type checking
if ($livetype) {
  Write-Host -ForegroundColor DarkCyan      "[live][TYPE]      Running static type analysis using mypy ..."
  & $runTypingFunc $PackageName $true $copytype $runTypingCopyFunc
  Write-Host -ForegroundColor DarkCyan      "[live][TYPE]      Static type analysis finished"
} elseif ($type) {
  Write-Host -ForegroundColor DarkCyan      "[Job2][TYPE]      Running static type analysis using mypy ..."
  Write-Host -ForegroundColor DarkCyan      "[SCRIPT]          Starting TypeChecking jobs ..."
  $typingJob = Start-Job -Name "TypeChecking" -ScriptBlock $runTypingFunc -ArgumentList $PackageName, $false, $copytype, $runTypingCopyFunc
}

# Documentation generation
if ($livedoc) {
  if ($typingJob) {
    $null = Wait-Job -Job $typingJob
    Write-Host                              "[live][DOC]       Awaited Job2:TypeChecking"
  }
  if ($testJob) {
    $null = Wait-Job -Job $testJob
    Write-Host                              "[live][DOC]       Awaited Job1:Test"
  }

  Write-Host -ForegroundColor DarkYellow    "[live][DOC]       Building documentation using Sphinx ..."
  if ($html) {
    Write-Host -ForegroundColor DarkYellow  "[live][HTML]      Building HTML documentation using Sphinx ..."
    & $compileHTMLDocFunc $PythonVersion $true $copyunit $copycov $copytype $runUnitCopyFunc $runCovCopyFunc $runTypingCopyFunc
  }
  if ($latex) {
    Write-Host -ForegroundColor DarkYellow  "[live][LaTeX]     Building LaTeX documentation using Sphinx ..."
    & $compileLaTeXDocFunc $PythonVersion $LaTeXDocument
  }
  if ($pdf) {
    Write-Host -ForegroundColor DarkYellow  "[live][PDF]       Building PDF documentation using LuaLaTeX ..."
    & $compilePDFDocFunc $LaTeXDocument
  }
  Write-Host -ForegroundColor DarkYellow    "[live][DOC]       Documentation finished"
} else {
  if ($html -or $latex -or $pdf) {
    Write-Host -ForegroundColor DarkGreen   "[SCRIPT]          Starting Documentation jobs ..."
  }

  if ($html) {
    Write-Host -ForegroundColor DarkYellow  "[Job3][HTML]      Building HTML documentation using Sphinx (waiting on Job1:Testing and Job2:Typing) ..."
    $docHTMLJob = Start-Job -Name "HTMLDoc" -ScriptBlock {
      param($typingJob, $testJob, $compileDocStr, $PyVersion, $copyUnit, $copyCov, $copyType, $runUnitCopyStr, $runCovCopyStr, $runTypingCopyStr)

      $compileDocFunc =    [ScriptBlock]::Create($compileDocStr)
      $runUnitCopyFunc =   [ScriptBlock]::Create($runUnitCopyStr)
      $runCovCopyFunc =    [ScriptBlock]::Create($runCovCopyStr)
      $runTypingCopyFunc = [ScriptBlock]::Create($runTypingCopyStr)

      if ($typingJob) {
        $null = Wait-Job -Job $typingJob
        Write-Host                          "[Job3][HTML]      Awaited Job2:TypeChecking"
      }
      if ($testJob) {
        $null = Wait-Job -Job $testJob
        Write-Host                          "[Job3][HTML]      Awaited Job1:Test"
      }

      & $compileDocFunc $PyVersion $false $copyUnit $copyCov $copyType $runUnitCopyFunc $runCovCopyFunc $runTypingCopyFunc
    } -ArgumentList $typingJob, $testJob, $compileHTMLDocFunc, $PythonVersion, $copyunit, $copycov, $copytype, $runUnitCopyFunc, $runCovCopyFunc, $runTypingCopyFunc
  }
  if ($latex) {
    Write-Host -ForegroundColor DarkYellow  "[Job4][LaTeX]     Building LaTeX documentation using Sphinx (waiting on Job1:Testing and Job2:Typing) ..."
    $docLaTeXJob = Start-Job -Name "LaTeXDoc" -ScriptBlock {
      param($typingJob, $testJob, $compileDocStr, $PyVersion, $LaTeXDocument)

      $compileDocFunc = [ScriptBlock]::Create($compileDocStr)

      if ($typingJob) {
        $null = Wait-Job -Job $typingJob
        Write-Host                          "[Job4][LaTeX]     Awaited Job2:TypeChecking"
      }
      if ($testJob) {
        $null = Wait-Job -Job $testJob
        Write-Host                          "[Job4][LaTeX]     Awaited Job1:Test"
      }

      & $compileDocFunc $PyVersion $LaTeXDocument
    } -ArgumentList $typingJob, $testJob, $compileLaTeXDocFunc, $PythonVersion, $LaTeXDocument
  }
  if ($pdf) {
    Write-Host -ForegroundColor DarkYellow  "[Job5][PDF]       Building PDF documentation using LuaLaTex (waiting on Job4:LaTeX) ..."
    $docPDFJob = Start-Job   -Name "PDFDoc"   -ScriptBlock {
      param($docLaTeXJob, $compileDocStr, $LaTeXDocument)

      $compileDocFunc = [ScriptBlock]::Create($compileDocStr)

      if ($docLaTeXJob) {
        $null = Wait-Job -Job $docLaTeXJob
        Write-Host "[Job5][PDF]       Awaited Job4:LaTeX"
      }
      & $compileDocFunc $LaTeXDocument
    } -ArgumentList $docLaTeXJob, $compilePDFDocFunc, $LaTeXDocument
  }
}

# Await jobs
if ($typingJob) {
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Waiting on TypeChecking job ..."
  $null = Wait-Job -Job $typingJob
  Write-Host -ForegroundColor DarkYellow    "[Job2][TYPE]      Static type checking finished"
}
if ($testJob) {
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Waiting on unit testing job ..."
  $null = Wait-Job -Job $testJob
  Write-Host -ForegroundColor DarkYellow    "[Job1][TEST]      Unit testing finished"
}
if ($docHTMLJob) {
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Waiting on HTML Documentation job ..."
  $null = Wait-Job -Job $docHTMLJob
  Write-Host -ForegroundColor DarkYellow    "[Job3][HTML]      HTML Documentation finished"
}
if ($docLaTeXJob) {
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Waiting on LaTeX Documentation job ..."
  $null = Wait-Job -Job $docLaTeXJob
  Write-Host -ForegroundColor DarkYellow    "[Job4][LaTeX]     LaTeX Documentation finished"
}
if ($docPDFJob) {
  Write-Host -ForegroundColor DarkGreen     "[SCRIPT]          Waiting on PDF Documentation job ..."
  $null = Wait-Job -Job $docPDFJob
  Write-Host -ForegroundColor DarkYellow    "[Job5][PDF]       PDF Documentation finished"
}

# Write collected outputs
if ($typingJob) {
  Write-Host -ForegroundColor DarkCyan      "================================================================================"
  if (-not $nooutput) {
    Receive-Job -Job $typingJob
  }
  Remove-Job  -Job $typingJob
}
if ($docHTMLJob) {
  Write-Host -ForegroundColor DarkYellow    "================================================================================"
  if (-not $nooutput) {
    Receive-Job -Job $docHTMLJob
  }
  Remove-Job  -Job $docHTMLJob
}
if ($docLaTeXJob) {
  Write-Host -ForegroundColor DarkYellow    "================================================================================"
  if (-not $nooutput) {
    Receive-Job -Job $docLaTeXJob
  }
  Remove-Job  -Job $docLaTeXJob
}
if ($docPDFJob) {
  Write-Host -ForegroundColor DarkYellow    "================================================================================"
  if (-not $nooutput) {
    Receive-Job -Job $docPDFJob
  }
  Remove-Job  -Job $docPDFJob
}
if ($testJob) {
  Write-Host -ForegroundColor DarkBlue      "================================================================================"
  if (-not $nooutput) {
    Receive-Job -Job $testJob
  }
  Remove-Job  -Job $testJob
}

Write-Host -ForegroundColor DarkGreen       "================================================================================"
Write-Host -ForegroundColor DarkGreen       "[SCRIPT]          Finished"
