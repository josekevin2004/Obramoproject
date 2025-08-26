// Initialize Chart
const ctx = document.getElementById('investmentChart').getContext('2d');
new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Desenvolvimento Web', 'Design UX/UI', 'App Mobile', 'DevOps', 'Outros'],
        datasets: [{
            data: [45, 25, 20, 7, 3],
            backgroundColor: [
                '#3B82F6', // Blue
                '#8B5CF6', // Purple  
                '#10B981', // Green
                '#F59E0B', // Yellow
                '#EF4444'  // Red
            ],
            borderWidth: 0,
            cutout: '60%'
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
                    usePointStyle: true,
                    font: {
                        size: 12
                    }
                }
            }
        }
    }
});

// Add some interactive elements
document.addEventListener('DOMContentLoaded', function () {
    // Simulate real-time updates
    setInterval(() => {
        const progressBars = document.querySelectorAll('.progress-fill');
        progressBars.forEach(bar => {
            const currentWidth = parseInt(bar.style.width);
            if (currentWidth < 100) {
                // Small random progress updates
                const increment = Math.random() * 0.5;
                bar.style.width = Math.min(100, currentWidth + increment) + '%';
            }
        });
    }, 5000);
});


