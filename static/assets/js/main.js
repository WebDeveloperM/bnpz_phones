$(document).ready(function () {

    if ($.fn.DataTable.isDataTable('#scrollVertical')) {
        $('#scrollVertical').DataTable().destroy();
    }


    $('#scrollVertical').DataTable({
        language: {
            lengthMenu: 'Показать: <select>' +
                '<option value="10">10</option>' +
                '<option value="25">25</option>' +
                '<option value="50">50</option>' +
                '<option value="100">100</option>' +
                '</select>',
            info: "Показано с _START_ по _END_ из _TOTAL_ записей",
            search: "Поиск:",
            paginate: {
                first: "Биринчи",
                last: "Последний",
                next: "Следующий",
                previous: "Предыдущий"
            },
            zeroRecords: "Информация не найдена"
        },
        scrollY: "100vh",
        scrollCollapse: true,
        paging: true
    });
})


document.addEventListener("DOMContentLoaded", function () {
    const translitMap = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'X', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'x', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    };

    function transliterate(text) {
        return text.split('').map(char => translitMap[char] || char).join('');
    }

    document.querySelectorAll("tbody tr").forEach(row => {
        const originalText = row.querySelector(".original-text-fio").textContent.trim();
        const translatedText = transliterate(originalText);
        row.querySelector(".translated-text-fio").textContent = translatedText;
    });

    document.querySelectorAll("tbody tr").forEach(row => {
        const originalText = row.querySelector(".original-text-jobs").textContent.trim();
        const translatedText = transliterate(originalText);
        row.querySelector(".translated-text-jobs").textContent = translatedText;
    });

    document.querySelectorAll("tbody tr").forEach(row => {
        const originalText = row.querySelector(".original-text-depart").textContent.trim();
        const translatedText = transliterate(originalText);
        row.querySelector(".translated-text-depart").textContent = translatedText;
    });

});
