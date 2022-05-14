/*
 Делает кнопку неактивной и показывает иконку загрузки.
 Применять к тегу button или a.
 */
function preloaderButton(elm) {
    var e = $(elm);
    e.html(
        '<i class="fa fa-spinner fa-spin" aria-hidden="true"></i>' + e.html()
    ).prop('disabled', true).click(function () {
        return false;
    });
}


/*
 Создает форму через ajax в модальном окне.
 */
function createModalAjax(modalId, url) {
    $.ajax({
        type: 'GET',
        url: url,
        success: function (data) {
            $(modalId + ' .modal-content').html(data);
        },
        error: function () {
            messageShow(
                'Произошла ошибка. обновите страницу и повторите попытку. Если ошибка повторится, обратитесь в \ ' +
                'службу поддержки.',
                'alert-danger');
            closeModal(modalId);
        }
    });

    $(modalId).modal();
    return false;
}


/*
 Сохраняет форму через ajax в модальном окне.
 */
function saveFormModal(modalId, formId) {
    var form = $(formId);

    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (data) {
            $(modalId + ' .modal-content').html(data);
        },
        error: function () {
            messageShow(
                'Произошла ошибка. обновите страницу и повторите попытку. Если ошибка повторится, обратитесь в \ ' +
                'службу поддержки.',
                'alert-danger');
            closeModal(modalId);
        }
    });

    $(modalId).modal();
    return false;
}


/*
 Сохраняет форму через ajax в контейнер.
 */
function saveFormContainer(containerId, formId) {
    var form = $(formId);

    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (data) {
            $(containerId).html(data);
        },
        error: function () {
            messageShow(
                'Произошла ошибка. обновите страницу и повторите попытку. Если ошибка повторится, обратитесь в \ ' +
                'службу поддержки.',
                'alert-danger');
        }
    });
}


/*
 Закрыть модальное окно.
 */
function closeModal(modalId) {
    $(modalId).modal('hide');
}


/*
 Вывести сообщение.
 */
function messageShow(msg, css_class) {
    var m = $('<div class="alert ' + css_class + ' fade in">\
        <button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>' +
        msg + '</div>');

    $('#alert').append(m);
    m.alert();
}


/*
 Устанавливает фокус на первый найденный input.
 */
function firstInputFocus(selector) {
    selector = selector || 'input:visible';
    var input = $(selector).first();
    input.focus();
}


/*
 Выводит форматированную стоимость.
 */
function priceFormat(data) {
    var price = Number.prototype.toFixed.call(parseFloat(data) || 0, 2),
        price_sep = price.replace(/(\D)/g, ".");
    return price_sep.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1 ");
}


/*
 Позволяет к любому select динамически добавить опцию "Другой".
 При выборе этой опции появляется input.
 Пользователь вводит название. После этого посредством ajax в БД создается новая запись.
 Эта запись добавляется в видео option в select и делается выбранной.

 Для работы нужен URL скрипта-обработчика нового значения (сохранение в БД).
 prepare - функция обработчик данных. Подготавливает данные перед передачей их по URL.

 Пример:
 function prepare(select, value) {
 return {country: $('#country').val(), value: value}
 }
 otherSelect($('#city'), '/ajax/city/', prepare);

 */
function otherSelect(elm, url, prepare) {
    var parent = elm.parent();

    // Добавляю опцию "Другой".
    elm.append(
        $("<option></option>")
            .html(gettext('Other'))
            .data('other', true)
            .attr('value', '')
    );

    elm.change(function () {
        if (!elm.find('option[data-other]').length) {
            // Если произошло ajax обновление списка, то снова добавляю опцию "Другой".
            elm.append(
                $("<option></option>")
                    .html(gettext('Other'))
                    .data('other', true)
                    .attr('value', '')
            );
        }

        if (elm.find('option:selected').data('other') == true) {
            // Прив выборе опции "Другой" создаю input с обработчиком изменения введенного текста.
            var input = $('<input type="text" class="form-control" data-other-input>');
            parent.append(input);

            setTimeout(function () {
                input.focus();
            }, 1);

            // При клике ENTER вызываю событие change для select.
            input.on('keydown', function (event) {
                if (event.keyCode == 13) {
                    input.change();
                    event.preventDefault();
                    return false;
                }
            });

            // Сохраняю введенное значение, добавляю его в select и делаю выбранным.
            input.change(function () {
                var value = $(this).val(),
                    data = {value: value};

                if (typeof prepare === "function") {
                    data = prepare(elm, value);
                }

                $.ajax({
                    type: 'GET',
                    url: url,
                    data: data,
                    dataType: 'json',
                    success: function (data) {
                        var opt = $('<option></option>')
                            .html(value)
                            .val(data.id)
                            .prop('selected', true);

                        elm.prepend(opt);

                        parent.find('input[data-other-input]').remove();
                    },
                    error: function () {
                        messageShow(
                            'Произошла ошибка. обновите страницу и повторите попытку. Если ошибка повторится, \
                            обратитесь в службу поддержки.',
                            'alert-danger');
                    }
                });
            });
        } else {
            parent.find('input[data-other-input]').remove();
        }
    });
}
