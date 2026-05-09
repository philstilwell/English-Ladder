function checkAnswer(btn) {
    const optionsContainer = btn.parentElement;

    Array.from(optionsContainer.children).forEach((button) => {
        button.style.backgroundColor = "#fff";
    });

    btn.style.backgroundColor = btn.dataset.bg;
    const feedbackDiv = optionsContainer.nextElementSibling;
    feedbackDiv.innerHTML = btn.dataset.feedback;
    feedbackDiv.style.color = btn.dataset.color;
}
