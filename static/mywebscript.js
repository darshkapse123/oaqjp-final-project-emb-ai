
function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();

    if (!textToAnalyze) {
        document.getElementById("system_response").innerText =
            "Please enter some text to analyze.";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                document.getElementById("system_response").innerText =
                    this.responseText;
            } else {
                document.getElementById("system_response").innerText =
                    "Unable to process your request. Please try again.";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
}
