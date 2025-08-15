const AUTH_EMAIL = "ahahkaur77@gmail.com";
// Replace the password below with the correct one.
const AUTH_PASSWORD = "Arsh2024";

document.getElementById("loginForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  if (email === AUTH_EMAIL && password === AUTH_PASSWORD) {
    sessionStorage.setItem("authed", "true");
    window.location.href = "home.html";
  } else {
    alert("Wrong riddle answer. Try again!");
  }
});
