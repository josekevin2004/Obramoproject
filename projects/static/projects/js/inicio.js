document.addEventListener('DOMContentLoaded', function () {

    const tabs = document.querySelectorAll('.dashboard-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', function () {
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });


    const stars = document.querySelectorAll('.fa-star.cursor-pointer');
    stars.forEach((star, index) => {
        star.addEventListener('click', function () {
            stars.forEach((s, i) => {
                if (i <= index) {
                    s.classList.add('text-yellow-400');
                    s.classList.remove('text-gray-300');
                } else {
                    s.classList.remove('text-yellow-400');
                    s.classList.add('text-gray-300');
                }
            });
        });

        star.addEventListener('mouseover', function () {
            stars.forEach((s, i) => {
                if (i <= index) {
                    s.classList.add('text-yellow-400');
                    s.classList.remove('text-gray-300');
                } else {
                    s.classList.remove('text-yellow-400');
                    s.classList.add('text-gray-300');
                }
            });
        });
    });
});