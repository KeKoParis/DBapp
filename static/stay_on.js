// При загрузке страницы
window.onload = function () {
    // Если в localStorage сохранено значение прокрутки
    if (localStorage.getItem('scrollPosition')) {
        // Прокрутите страницу до сохраненного значения
        window.scrollTo(0, localStorage.getItem('scrollPosition'));
    }

    // При прокрутке страницы
    window.onscroll = function () {
        // Сохраните текущую позицию прокрутки в localStorage
        localStorage.setItem('scrollPosition', window.pageYOffset);
    };
};