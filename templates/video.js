const video = document.getElementById('video');
function showSubtitle(startTime, text) {
    const subtitle = document.createElement('div');
    subtitle.textContent = text;
    document.getElementById('overlay').appendChild(subtitle);
}
showSubtitle(5, 'Hello, world!');
video.addEventListener('timeupdate', () => {
    const currentTime = video.currentTime;
    showSubtitle(currentTime, 'Hello, world!');
});
  