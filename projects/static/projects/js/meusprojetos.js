document.addEventListener('DOMContentLoaded', function() {
            // Filter functionality
            const filterBtns = document.querySelectorAll('.filter-btn');
            const projectCards = document.querySelectorAll('.project-card');

            filterBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    // Remove active class from all buttons
                    filterBtns.forEach(b => b.classList.remove('filter-active'));
                    // Add active class to clicked button
                    this.classList.add('filter-active');

                    const filter = this.dataset.filter;
                    
                    projectCards.forEach(card => {
                        if (filter === 'todos' || card.dataset.status === filter) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                });
            });

            // View toggle functionality
            const viewToggleBtns = document.querySelectorAll('.view-toggle');
            const projectsContainer = document.getElementById('projectsContainer');

            viewToggleBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    // Remove active class from all buttons
                    viewToggleBtns.forEach(b => {
                        b.classList.remove('bg-blue-600', 'text-white');
                        b.classList.add('hover:bg-gray-50');
                    });
                    
                    // Add active class to clicked button
                    this.classList.add('bg-blue-600', 'text-white');
                    this.classList.remove('hover:bg-gray-50');

                    const view = this.dataset.view;
                    
                    if (view === 'list') {
                        // Switch to list view (you can implement this)
                        console.log('List view selected');
                    } else {
                        // Cards view (default)
                        console.log('Cards view selected');
                    }
                });
            });

            // Search functionality
            const searchInput = document.querySelector('input[placeholder="Buscar projetos..."]');
            searchInput.addEventListener('input', function() {
                const searchTerm = this.value.toLowerCase();
                
                projectCards.forEach(card => {
                    const title = card.querySelector('h3').textContent.toLowerCase();
                    const description = card.querySelector('p').textContent.toLowerCase();
                    
                    if (title.includes(searchTerm) || description.includes(searchTerm)) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });

            // Simulate progress updates
            setInterval(() => {
                const progressBars = document.querySelectorAll('.progress-fill');
                progressBars.forEach(bar => {
                    const currentWidth = parseInt(bar.style.width);
                    if (currentWidth < 100) {
                        const increment = Math.random() * 0.3;
                        bar.style.width = Math.min(100, currentWidth + increment) + '%';
                        
                        // Update progress text
                        const progressText = bar.parentElement.previousElementSibling.querySelector('span:last-child');
                        progressText.textContent = Math.round(parseFloat(bar.style.width)) + '%';
                    }
                });
            }, 8000);
        });