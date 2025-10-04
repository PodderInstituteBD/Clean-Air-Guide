function showResult() {
    let checkboxes = document.querySelectorAll('#tips-form input[type="checkbox"]');
    let count = 0;

    checkboxes.forEach(cb => {
        if (cb.checked) {
            count++;
        }
    });

    let result = document.getElementById("result");

    if (count === 0) {
        result.textContent = "😕 Try to do at least one action today!";
    } else if (count < 3) {
        result.textContent = "👍 Good start! You completed " + count + " actions.";
    } else {
        result.textContent = "🎉 Amazing! You completed " + count + " clean air actions today!";
    }
}
