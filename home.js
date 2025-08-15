if (sessionStorage.getItem("authed") !== "true") {
  window.location.href = "index.html";
}

function updateCountdown() {
  const now = new Date();
  const upcoming = songs
    .map((s) => new Date(s.releaseDate))
    .filter((d) => d > now)
    .sort((a, b) => a - b)[0];

  const el = document.getElementById("countdown");
  if (!upcoming) {
    el.textContent = "All songs released!";
    return;
  }
  const diff = upcoming - now;
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((diff / (1000 * 60)) % 60);
  const seconds = Math.floor((diff / 1000) % 60);
  el.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}
setInterval(updateCountdown, 1000);
updateCountdown();

const list = document.getElementById("songList");
songs.forEach((song) => {
  const li = document.createElement("li");
  const h2 = document.createElement("h2");
  h2.textContent = song.title;
  li.appendChild(h2);

  const details = document.createElement("details");
  const summary = document.createElement("summary");
  summary.textContent = "Lyrics";
  details.appendChild(summary);
  const pre = document.createElement("pre");
  pre.textContent = song.lyrics;
  details.appendChild(pre);
  li.appendChild(details);

  const link = document.createElement("a");
  link.textContent = "Download";
  link.href = song.file || "#";
  link.download = "";
  li.appendChild(link);

  list.appendChild(li);
});
