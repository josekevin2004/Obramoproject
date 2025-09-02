// ----- CÓDIGO UNIFICADO E CORRIGIDO -----

// Espera o documento carregar completamente antes de executar qualquer script.
document.addEventListener("DOMContentLoaded", function () {

  // ===== State (Estado da Aplicação) =====
  let currentStep = 1;
  const totalSteps = 5;
  let userType = ""; // 'client' ou 'professional'

  // ===== Elements (Elementos do DOM) =====
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const submitBtn = document.getElementById("submitBtn");
  const registerForm = document.getElementById("registerForm");

  // Elementos da barra de progresso
  const progressBar = document.getElementById("progressBar");
  const currentStepEl = document.getElementById("currentStep");
  const progressPercentEl = document.getElementById("progressPercent");

  // Conteúdos dinâmicos da Etapa 3
  const professionalSkills = document.getElementById("professionalSkills");
  const clientNeeds = document.getElementById("clientNeeds");
  
  // Checkbox de termos (Etapa 4)
  const termsCheck = document.getElementById("termsCheck");


  // ===== Functions (Funções) =====

  /**
   * Mostra uma etapa específica do formulário e atualiza a interface.
   * @param {number} step - O número da etapa a ser exibida.
   */
  function showStep(step) {
      // Esconde todas as etapas
      document.querySelectorAll(".step-content").forEach(s => s.classList.add("hidden"));
      
      // Mostra a etapa correta
      const el = document.getElementById(`step${step}`);
      if (el) el.classList.remove("hidden");

      // Lógica para a Etapa 3: mostra o conteúdo do cliente ou profissional
      if (step === 3) {
          if (userType === "professional") {
              professionalSkills.classList.remove("hidden");
              clientNeeds.classList.add("hidden");
          } else {
              clientNeeds.classList.remove("hidden");
              professionalSkills.classList.add("hidden");
          }
      }

      // Atualiza a barra de progresso
      const pct = Math.round((step / totalSteps) * 100);
      progressBar.style.width = `${pct}%`;
      currentStepEl.textContent = step.toString();
      progressPercentEl.textContent = pct.toString();

      // Habilita/desabilita os botões de navegação
      prevBtn.disabled = step === 1;
      nextBtn.style.display = (step === totalSteps) ? "none" : "inline-flex";

      // Regra especial para a Etapa 1 (só pode avançar se escolher um tipo)
      if (step === 1) {
          nextBtn.disabled = userType === "";
      } else {
          nextBtn.disabled = false;
      }
  }

  /**
   * Avança para a próxima etapa do formulário.
   */
  function goNext() {
      if (currentStep >= totalSteps) return;

      // Validação da Etapa 2 (Informações Básicas)
      if (currentStep === 2) {
          // Usa a validação nativa do navegador para os campos do formulário
          if (!registerForm.checkValidity()) {
              registerForm.reportValidity();
              return; // Impede de avançar se o formulário for inválido
          }
      }

      // Validação da Etapa 4 (Termos e Condições)
      if (currentStep === 4 && !termsCheck.checked) {
          alert("Você precisa aceitar os Termos de Uso e a Política de Privacidade para continuar.");
          return;
      }

      currentStep++;
      showStep(currentStep);
  }

  /**
   * Retorna para a etapa anterior do formulário.
   */
  function goPrev() {
      if (currentStep <= 1) return;
      currentStep--;
      showStep(currentStep);
  }


  // ===== Event Listeners (Escutadores de Eventos) =====

  // 1. Clique nos cards de tipo de usuário
  document.querySelectorAll(".user-type-card").forEach(card => {
      card.addEventListener("click", () => {
          document.querySelectorAll(".user-type-card").forEach(c => c.classList.remove("selected"));
          card.classList.add("selected");
          userType = card.dataset.type || "";
          
          // NOVO: Atualiza o campo oculto do formulário com o tipo de usuário
          document.getElementById("userTypeInput").value = userType; 

          // Habilita o botão "Próximo"
          if (currentStep === 1) nextBtn.disabled = false;
      });
  });

  // 2. Clique nas tags de habilidades (permite selecionar/deselecionar)
  document.querySelectorAll(".skill-tag").forEach(tag => {
      tag.addEventListener("click", () => tag.classList.toggle("selected"));
  });

  // 3. Botões de navegação
  prevBtn.addEventListener("click", goPrev);
  nextBtn.addEventListener("click", goNext);
  
  // 4. Efeito visual no botão de cadastro
  if (submitBtn) {
      submitBtn.addEventListener("click", function() {
          this.classList.remove("btn-success");
          this.classList.add("bg-blue-600", "hover:bg-blue-700");
          this.textContent = "Enviando...";
      });
  }

  // ===== Initialization (Inicialização) =====
  // Mostra a primeira etapa quando a página carrega.
  showStep(currentStep);

});