(function() {
    var $terminalIn, $terminalOut, $window, printCmd;
  
    $terminalIn = $('.terminal-input input');
  
    $terminalOut = $('.terminal-output');
  
    $window = $('.window');
  
    $('form').on('submit', function(e) {
      var $input;
      e.preventDefault();
      //# Get Input
      $input = $terminalIn.val();
      //# Display Output
      $terminalOut.append(printCmd($input));
      //# Clear Input
      $terminalIn.val("");
      //# Keep focused on input
      return $('.terminal').animate({
        scrollTop: $(".terminal")[0].scrollHeight,
        100: 100
      });
    });
  
    //# Template for cmd line print
    printCmd = function($input) {
      return `<div class='cmd-container'> <span class='terminal-path'> <i class='terminal-blue'>~ / </i> <i class='terminal-red'>❯</i> <i class='terminal-yellow'>❯</i> <i class='terminal-green'>❯</i> </span> <span class='eval'>${$input}</span> </div>`;
    };
  
    //# Focus to input on window click
    $window.on('click', function(e) {
      return $terminalIn.focus();
    });
  
  }).call(this);
  
  //# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiPGFub255bW91cz4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7QUFBQSxNQUFBLFdBQUEsRUFBQSxZQUFBLEVBQUEsT0FBQSxFQUFBOztFQUFBLFdBQUEsR0FBYyxDQUFBLENBQUUsdUJBQUY7O0VBQ2QsWUFBQSxHQUFlLENBQUEsQ0FBRSxrQkFBRjs7RUFDZixPQUFBLEdBQVUsQ0FBQSxDQUFFLFNBQUY7O0VBRVYsQ0FBQSxDQUFFLE1BQUYsQ0FBUyxDQUFDLEVBQVYsQ0FBYSxRQUFiLEVBQXVCLFFBQUEsQ0FBQyxDQUFELENBQUE7QUFDdkIsUUFBQTtJQUFFLENBQUMsQ0FBQyxjQUFGLENBQUEsRUFBRjs7SUFFRSxNQUFBLEdBQVMsV0FBVyxDQUFDLEdBQVosQ0FBQSxFQUZYOztJQUlFLFlBQVksQ0FBQyxNQUFiLENBQW9CLFFBQUEsQ0FBUyxNQUFULENBQXBCLEVBSkY7O0lBTUUsV0FBVyxDQUFDLEdBQVosQ0FBZ0IsRUFBaEIsRUFORjs7V0FRRSxDQUFBLENBQUUsV0FBRixDQUFjLENBQUMsT0FBZixDQUNFO01BQUMsU0FBQSxFQUFXLENBQUEsQ0FBRSxXQUFGLENBQWMsQ0FBQyxDQUFELENBQUcsQ0FBQyxZQUE5QjtNQUE0QyxLQUFBO0lBQTVDLENBREY7RUFUcUIsQ0FBdkIsRUFKQTs7O0VBZ0JBLFFBQUEsR0FBVyxRQUFBLENBQUMsTUFBRCxDQUFBO1dBQ1QsQ0FBQSx3S0FBQSxDQUFBLENBT3lCLE1BUHpCLENBQUEsY0FBQTtFQURTLEVBaEJYOzs7RUE0QkEsT0FBTyxDQUFDLEVBQVIsQ0FBVyxPQUFYLEVBQW9CLFFBQUEsQ0FBQyxDQUFELENBQUE7V0FDbEIsV0FBVyxDQUFDLEtBQVosQ0FBQTtFQURrQixDQUFwQjtBQTVCQSIsInNvdXJjZXNDb250ZW50IjpbIiR0ZXJtaW5hbEluID0gJCgnLnRlcm1pbmFsLWlucHV0IGlucHV0JylcbiR0ZXJtaW5hbE91dCA9ICQoJy50ZXJtaW5hbC1vdXRwdXQnKVxuJHdpbmRvdyA9ICQoJy53aW5kb3cnKVxuXG4kKCdmb3JtJykub24gJ3N1Ym1pdCcsIChlKSAtPlxuICBlLnByZXZlbnREZWZhdWx0KClcbiAgIyMgR2V0IElucHV0XG4gICRpbnB1dCA9ICR0ZXJtaW5hbEluLnZhbCgpXG4gICMjIERpc3BsYXkgT3V0cHV0XG4gICR0ZXJtaW5hbE91dC5hcHBlbmQocHJpbnRDbWQoJGlucHV0KSlcbiAgIyMgQ2xlYXIgSW5wdXRcbiAgJHRlcm1pbmFsSW4udmFsKFwiXCIpXG4gICMjIEtlZXAgZm9jdXNlZCBvbiBpbnB1dFxuICAkKCcudGVybWluYWwnKS5hbmltYXRlKFxuICAgIHtzY3JvbGxUb3A6ICQoXCIudGVybWluYWxcIilbMF0uc2Nyb2xsSGVpZ2h0LCAxMDB9KVxuIyMgVGVtcGxhdGUgZm9yIGNtZCBsaW5lIHByaW50XG5wcmludENtZCA9ICgkaW5wdXQpIC0+XG4gIFwiPGRpdiBjbGFzcz0nY21kLWNvbnRhaW5lcic+XG4gICAgICA8c3BhbiBjbGFzcz0ncGF0aCc+XG4gICAgICAgIDxpIGNsYXNzPSdibHVlJz5+IC8gPC9pPlxuICAgICAgICA8aSBjbGFzcz0ncmVkJz7ina88L2k+XG4gICAgICAgIDxpIGNsYXNzPSd5ZWxsb3cnPuKdrzwvaT5cbiAgICAgICAgPGkgY2xhc3M9J2dyZWVuJz7ina88L2k+XG4gICAgICA8L3NwYW4+XG4gICAgICA8c3BhbiBjbGFzcz0nZXZhbCc+I3skaW5wdXR9PC9zcGFuPlxuICAgIDwvZGl2PlwiXG5cbiMjIEZvY3VzIHRvIGlucHV0IG9uIHdpbmRvdyBjbGlja1xuJHdpbmRvdy5vbiAnY2xpY2snLCAoZSktPlxuICAkdGVybWluYWxJbi5mb2N1cygpIl19
  //# sourceURL=coffeescript