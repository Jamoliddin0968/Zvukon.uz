// ------------------------------------------------------ //
// For demo purposes, can be deleted
// ------------------------------------------------------ //
var videos = document.getElementsByTagName('video');
var isPageVisible = true;

// Pause all videos when page visibility changes
document.addEventListener("visibilitychange", function() {
  if (document.hidden) {
    isPageVisible = false;
    for (var i = 0; i < videos.length; i++) {
      if (!videos[i].paused) {
        videos[i].pause();
      }
    }
  } else {
    isPageVisible = true;
    for (var i = 0; i < videos.length; i++) {
      if (!videos[i].paused && isVideoVisible(videos[i])) {
        videos[i].currentTime = 0;
        videos[i].play();
      }
    }
  }
});

// Pause videos when they become hidden
document.addEventListener("visibilitychange", function() {
  if (!isPageVisible) {
    for (var i = 0; i < videos.length; i++) {
      if (!videos[i].paused) {
        videos[i].pause();
      }
    }
  }
});

// Play videos when they become visible
document.addEventListener("visibilitychange", function() {
  if (isPageVisible) {
    for (var i = 0; i < videos.length; i++) {
      if (!videos[i].paused && isVideoVisible(videos[i])) {
        videos[i].currentTime = 0;
        videos[i].play();
      }
    }
  }
});

// Helper function to check if a video is visible
function isVideoVisible(video) {
  var rect = video.getBoundingClientRect();
  var isVisible = (rect.top >= 0 && rect.bottom <= window.innerHeight);
  return isVisible;
}

document.addEventListener("DOMContentLoaded", function () {
    // Asigning Alternative stylesheet & insert it in its place
    var stylesheet = document.getElementById("theme-stylesheet");
    var alternateStylesheet = document.createElement("link");
    alternateStylesheet.setAttribute("id", "new-stylesheet");
    alternateStylesheet.setAttribute("rel", "stylesheet");
    stylesheet.parentNode.insertBefore(alternateStylesheet, stylesheet.nextSibling);

    // Style Switcher
    var styleSwitcher = document.getElementById("colour");
    styleSwitcher.addEventListener("change", function () {
        var alternateColor = styleSwitcher.value;
        alternateStylesheet.setAttribute("href", alternateColor);
        Cookies.set("switcherColor", alternateColor, { expires: 365, path: "/" });
    });

    var theCookie = Cookies.get("switcherColor");
    if (theCookie) {
        alternateStylesheet.setAttribute("href", theCookie);
    }
});


