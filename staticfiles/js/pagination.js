var infinite = new Waypoint.Infinite({
  element: $('.infinite-container')[0],
  offset: 'bottom-in-view',
  onBeforePageLoad: function () {
    $('.paginate').show();
  },
  onAfterPageLoad: function () {
    $('.paginate').hide();
    $(".infinite-item").css("opacity","1");
  }
});