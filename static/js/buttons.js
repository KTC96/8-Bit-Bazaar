document.addEventListener('DOMContentLoaded', function() {
  var buttons = document.querySelectorAll('.btn');

  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('mousedown', function() {
      this.classList.add('btn-active');
    });
    buttons[i].addEventListener('mouseup', function() {
      this.classList.remove('btn-active');
    });
    buttons[i].addEventListener('mouseleave', function() {
      this.classList.remove('btn-center', 'btn-right', 'btn-left', 'btn-active');
    });
    buttons[i].addEventListener("mousemove", function(e) {
      var leftOffset = this.getBoundingClientRect().left;
      var btnWidth = this.offsetWidth;
      var myPosX = e.pageX;
      var newClass = "";
      if (myPosX < (leftOffset + 0.3 * btnWidth)) {
        newClass = 'btn-left';
      } else {
        if (myPosX > (leftOffset + 0.65 * btnWidth)) {
          newClass = 'btn-right';
        } else {
          newClass = 'btn-center';
        }
      }
      var clearedClassList = this.className.replace(/btn-center|btn-right|btn-left/gi, "").trim();
      this.className = clearedClassList + " " + newClass;
    });
  }
});
