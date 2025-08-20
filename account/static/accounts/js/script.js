// ===== State =====
let currentStep = 1;
const totalSteps = 5;
let userType = ""; // 'client' | 'professional'

// ===== Elements =====
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const progressBar = document.getElementById("progressBar");
const currentStepEl = document.getElementById("currentStep");
const progressPercentEl = document.getElementById("progressPercent");

// Step 3 dynamic containers
const professionalSkills = document.getElementById("professionalSkills");
const clientNeeds = document.getElementById("clientNeeds");

// Terms checkbox (step 4)
const termsCheck = document.getElementById("termsCheck");

// ===== Helpers =====
function showStep(step) {
  // hide all
  document.querySelectorAll(".step-content").forEach(s => s.classList.add("hidden"));
  // show requested
  const el = document.getElementById(`step${step}`);
  if (el) el.classList.remove("hidden");

  // dynamic content on step 3
  if (step === 3) {
    if (userType === "professional") {
      professionalSkills.classList.remove("hidden");
      clientNeeds.classList.add("hidden");
    } else {
      clientNeeds.classList.remove("hidden");
      professionalSkills.classList.add("hidden");
    }
  }

  // progress
  const pct = Math.round((step / totalSteps) * 100);
  progressBar.style.width = `${pct}%`;
  currentStepEl.textContent = step.toString();
  progressPercentEl.textContent = pct.toString();

  // nav buttons
  prevBtn.disabled = step === 1;
  if (step === totalSteps) {
    nextBtn.style.display = "none";
  } else {
    nextBtn.style.display = "inline-flex";
  }

  // step 1 guard (need userType to enable next)
  if (step === 1) {
    nextBtn.disabled = userType === "";
  } else {
    nextBtn.disabled = false;
  }
}

function goNext() {
  if (currentStep >= totalSteps) return;

  // Guards
  if (currentStep === 1 && !userType) {
    alert("Por favor, selecione como você pretende usar a plataforma.");
    return;
  }

  // (Opcional) exemplo simples de validação no passo 4: aceitar termos
  if (currentStep === 4 && !termsCheck.checked) {
    alert("Você precisa aceitar os Termos de Uso e a Política de Privacidade para continuar.");
    return;
  }

  currentStep++;
  showStep(currentStep);
}

function goPrev() {
  if (currentStep <= 1) return;
  currentStep--;
  showStep(currentStep);
}

// ===== Listeners =====
// User type cards
document.querySelectorAll(".user-type-card").forEach(card => {
  card.addEventListener("click", () => {
    document.querySelectorAll(".user-type-card").forEach(c => c.classList.remove("selected"));
    card.classList.add("selected");
    userType = card.dataset.type || "";
    // enable next on step 1
    if (currentStep === 1) nextBtn.disabled = userType === "";
  });
});

// Skill tags multi-select
function attachSkillTagHandlers(scope = document) {
  scope.querySelectorAll(".skill-tag").forEach(tag => {
    tag.addEventListener("click", () => tag.classList.toggle("selected"));
  });
}
attachSkillTagHandlers(document);

// Nav buttons
prevBtn.addEventListener("click", goPrev);
nextBtn.addEventListener("click", goNext);

// Init
showStep(currentStep);

