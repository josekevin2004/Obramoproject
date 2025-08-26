document.addEventListener('DOMContentLoaded', function() {
  // Seleciona os links do menu
  const navInicio = document.querySelector('nav a[href="#home"]');
  const navBuscar = document.querySelector('nav a[href="#search"]');
  const navComoFunciona = document.querySelector('nav a[href="#how-it-works"]');
  const navProfessionals = document.querySelector('nav a[href="#"]');
  const navContact = document.querySelector('nav a[href="#contact"]');
  

  function setActiveBar(activeLink) {
    [navInicio, navBuscar, navComoFunciona, navProfessionals, navContact].forEach(link => {
      link.classList.remove('border-b-4', 'border-blue-600', 'text-blue-600');
    });
    activeLink.classList.add('border-b-4', 'border-blue-600', 'text-blue-600');
  }

  // Inicialmente deixa "Início" ativo
  setActiveBar(navInicio);

  navInicio.addEventListener('click', function(e) {
    setActiveBar(navInicio);
  });
  navBuscar.addEventListener('click', function(e) {
    setActiveBar(navBuscar);
  });
  navComoFunciona.addEventListener('click', function(e) {
    setActiveBar(navComoFunciona);
   });
    navProfessionals.addEventListener('click', function(e) {
        setActiveBar(navProfessionals);
    });
    navContact.addEventListener('click', function(e) {
        setActiveBar(navContact);
    });
  });

