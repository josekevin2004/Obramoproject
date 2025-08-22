        // Specialty Distribution Chart
        const ctx = document.getElementById('specialtyChart').getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Desenvolvimento Web', 'Design UX/UI', 'Mobile', 'DevOps', 'Outros'],
                datasets: [{
                    data: [35, 25, 20, 12, 8],
                    backgroundColor: [
                        '#3B82F6',
                        '#8B5CF6',
                        '#10B981',
                        '#F59E0B',
                        '#EF4444'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 20,
                            usePointStyle: true
                        }
                    }
                }
            }
        });

        // Add interactive effects
        document.addEventListener('DOMContentLoaded', function () {
            // Animate progress bars
            const progressBars = document.querySelectorAll('.progress-bar');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 500);
            });

            // Add search functionality
            const searchInput = document.querySelector('input[placeholder="Buscar profissionais..."]');
            searchInput.addEventListener('input', function (e) {
                // Simulate search functionality
                console.log('Searching for:', e.target.value);
            });
        });