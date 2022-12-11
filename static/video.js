var rng = Math.floor(Math.random() * 4)+1;
var video = document.createElement('video');
video.muted = true;
video.loop = true;
video.autoplay = true;
video.poster = "static/first-frame" + String(rng) + ".png";
video.id = "bg-video"
var source = document.createElement('source');
source.src = "static/bg" + String(rng) + ".webm";
source.type = "video/webm";
video.appendChild(source);
document.body.appendChild(video);