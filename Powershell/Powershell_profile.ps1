python -u "C:\Users\User\projects\Scripts\Python\welcome_message.py"
Write-Host "Today is $(Get-Date)" -ForegroundColor Yellow

function llama{
	ollama run llama3.2:3b
}

function synclist {
    # Start the Flask app in a background job
	Write-Host "Running Script..."
    $flaskJob = Start-Job -ScriptBlock {
	cd "c:\Users\User\projects\Canvas2DoIst"
        python app.py
    }

    Start-Sleep -Seconds 1

	Write-Host "Accessing Assignments..."
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/sync-assignments" -UseBasicP
    Write-Host "Response Status Code: $($response.StatusCode)"

    # Stop the Flask job
    Stop-Job -Job $flaskJob
    Remove-Job -Job $flaskJob

    Write-Host "Done"
}


function ytmp3 {
	python -u "C:\Users\User\projects\Scripts\Python\ytDownload.py"
	explorer "C:\Users\User\Videos\Downloads"
}

function spotify{
	python -u "c:\Users\User\projects\Music-enter-room\spotipy_ting.py"
}

# Projects
function tda {
	cd C:\Users\User\projects\TDA_studies
	code .
}

function canvas2doist {
	cd C:\Users\User\projects\Canvas2DoIst
	code .
}

function ai {
	cd C:\Users\User\projects\Fall_24\AI-Principles-and-Practices
	code .
}

function whitebox {
	cd C:\Users\User\projects\WhiteBox
	code .
}

function gymapp {
	cd C:\Users\User\projects\GymApp_cashnode
	code .
}

function adcs {
	cd C:\Users\User\projects\PyMACS
	code .
}