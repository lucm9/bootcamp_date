const form = document.getElementById('voteForm');
const message = document.getElementById('message');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const selectedVote = document.querySelector('input[name="vote"]:checked');
  if (selectedVote) {
    // Send vote data to backend using fetch or similar
    fetch('/submit-vote', {
      method: 'POST',
      body: JSON.stringify({ vote: selectedVote.value })
    })
    .then(response => response.json())
    .then(data => {
      message.textContent = data.message;
    })
    .catch(error => {
      message.textContent = "Error submitting vote: " + error.message;
    });
  } else {
    message.textContent = "Please select a date option.";
  }
});
