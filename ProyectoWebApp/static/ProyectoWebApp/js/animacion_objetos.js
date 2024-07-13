$(document).ready(function() {
  // Trigger the creation of logos immediately upon page load
  createLogos();

  // Set interval to create new logos every 3 seconds
  setInterval(createLogos, 3000);

  function createLogos() {
    // Create two logos with different images and classes
    createLogo('/static/ProyectoWebApp/img/pelotac.png', 'logo1');
    createLogo('/static/ProyectoWebApp/img/pelotar.png', 'logo2');
  }

  function createLogo(imageUrl, className) {
    // Create a new div element with the specified class
    var $logo = $('<div class="bubble ' + className + '"></div>');

    // Random size for the logos between 80px and 150px
    var size = Math.random() * (150 - 80) + 80;

    // Random horizontal position within the window width
    var left = Math.random() * ($(window).width() - size);

    // Set size, background image, and position of the logo
    $logo.css({
      width: size + 'px',
      height: size + 'px',
      left: left + 'px',
      top: '100%', // Start from the bottom of the window
      backgroundImage: 'url(' + imageUrl + ')',
      position: 'absolute',
    });

    // Add the logo to the '#bubblesContainer' container
    $('#bubblesContainer').append($logo);

    // Click event to remove the logo when clicked
    $logo.click(function() {
      $(this).stop().fadeOut(500, function() {
        $(this).remove();
      });
    });

    // Animation: move logo upwards and remove it when it reaches the top
    $logo.animate({ top: '-20%' }, 10000, 'linear', function() {
      $(this).remove();
    });
  }
});
