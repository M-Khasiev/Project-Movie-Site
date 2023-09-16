//подгрузить еще по кнопке, если все элемнты подгружены, скрывает кнопку
 $(window).on('load', function() {
    initTwenty();
  });

  // Фото, до и после
//  function initTwenty() {
//    $(".twentytwenty").twentytwenty({
//      no_overlay: false, // Не показывать наложение было, стало, true скрыть
//      // Перемещать ползунок при наведении курсора мыши
//      move_slider_on_hover: false,
//      // Разрешить пользователю проводить пальцем в любом месте
//      // изображения для управления движением ползунка.
//      move_with_handle_only: true,
//      before_label: 'До',
//      after_label: 'После'
//    });
//  }

  $(document).ready(function() {
    var list = $(".gggggggg .twentytwenty");
    var numToShow = 1; //сколько показывать элементов
    var button = $("button");
    var numInList = list.length;
    list.hide();
    if (numInList > numToShow) {
      button.show();
    }
    list.slice(0, numToShow).show();
    button.click(function() {
      var showing = list.filter(':visible').length;
      list.slice(showing - 1, showing + numToShow).fadeIn();
      var nowShowing = list.filter(':visible').length;
      if (nowShowing >= numInList) {
        button.hide();
      }
      initTwenty();
    });
  });