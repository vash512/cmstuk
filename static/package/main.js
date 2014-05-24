$(document).ready(function() {
  $("#FFCvid").fitVids();
  var owl = $("#owl-demo");
 
  owl.owlCarousel({
    navigation : true, // Show next and prev buttons
    slideSpeed : 300,
    paginationSpeed : 400,
    singleItem:true,
    navigationText : ["Anterior", "Siguiente"]
  });

  $(".next").click(function(){
    owl.trigger('owl.next');
  })
  $(".prev").click(function(){
    owl.trigger('owl.prev');
  })

   
  var time = 8; // time in seconds
 
  var $progressBar,
      $bar, 
      $elem, 
      isPause, 
      tick,
      percentTime;
 
    //Init the carousel
  var owlProgramas = $("#owl-Programas");
  owlProgramas.owlCarousel({
    slideSpeed : 500,
    paginationSpeed : 500,
    items : 2,
    itemsDesktop : [1199,2],
    itemsDesktopSmall : [980,2],
    itemsTablet: [768,1],
    itemsTabletSmall: [480, 1],
    itemsMobile : [320,1],
    afterInit : progressBar,
    afterMove : moved,
    startDragging : pauseOnDragging,
    navigation: true,
    navigationText: [
        "Anterior",
        "Siguiente"
        ]
  });
  //Init progressBar where elem is $("#owl-demo")
  function progressBar(elem){
    $elem = elem;
    //build progress bar elements
    buildProgressBar();
    //start counting
    start();
  }
  //create div#progressBar and div#bar then prepend to $("#owl-demo")
  function buildProgressBar(){
    $progressBar = $("<div>",{
      id:"progressBar"
    });
    $bar = $("<div>",{
      id:"bar"
    });
    $progressBar.append($bar).prependTo($elem);
  }
 
  function start() {
    //reset timer
    percentTime = 0;
    isPause = false;
    //run interval every 0.01 second
    tick = setInterval(interval, 10);
  };
 
  function interval() {
    if(isPause === false){
      percentTime += 1 / time;
      $bar.css({
         width: percentTime+"%"
       });
      //if percentTime is equal or greater than 100
      if(percentTime >= 100){
        //slide to next item 
        $elem.trigger('owl.next')
      }
    }
  }
 
  //pause while dragging 
  function pauseOnDragging(){
    isPause = true;
  }
  //moved callback
  function moved(){
    //clear interval
    clearTimeout(tick);
    //start again
    start();
  }
  //uncomment this to make pause on mouseover 
  // $elem.on('mouseover',function(){
  //   isPause = true;
  // })
  // $elem.on('mouseout',function(){
  //   isPause = false;
  // })   
});