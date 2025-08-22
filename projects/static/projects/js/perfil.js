// Toggle switches functionality
        document.querySelectorAll('.toggle-switch input').forEach(toggle => {
            toggle.addEventListener('change', function() {
                if (this.checked) {
                    console.log('Configuração ativada');
                } else {
                    console.log('Configuração desativada');
                }
            });
        });

        // Button click handlers
        document.querySelectorAll('.btn').forEach(button => {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                const buttonText = this.textContent.trim();
                
                if (buttonText === 'Salvar Alterações') {
                    alert('Alterações salvas com sucesso!');
                } else if (buttonText === 'Excluir Conta') {
                    if (confirm('Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.')) {
                        alert('Solicitação de exclusão registrada. Você receberá um email com mais instruções.');
                    }
                } else if (buttonText === 'Ativar 2FA') {
                    alert('Redirecionando para configuração de autenticação de dois fatores...');
                } else {
                    console.log('Botão clicado:', buttonText);
                }
            });
        });

        // Form validation
        document.querySelectorAll('.form-control').forEach(input => {
            input.addEventListener('blur', function() {
                if (this.type === 'email' && this.value) {
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(this.value)) {
                        this.style.borderColor = '#e74a3b';
                    } else {
                        this.style.borderColor = '#d1d3e2';
                    }
                }
            });
        });