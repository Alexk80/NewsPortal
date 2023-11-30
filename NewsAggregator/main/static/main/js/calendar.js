if (!Modernizr.inputtypes.date) {
    $("input[type=date]").datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        minDate: '2000-01-01',
        maxDate: '2020-12-31',
        onSelect: function(selectedDate) {
            var id = $(this).attr("id");
            if (id == "minDate") {
                $("#calendar").datepicker('option', 'minDate', selectedDate);
            } else if (id == "maxDate") {
                $("#calendar").datepicker('option', 'maxDate', selectedDate);
            }
        }
    });

}