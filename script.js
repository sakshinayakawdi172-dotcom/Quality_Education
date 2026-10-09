document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', (event) => {
      const email = form.querySelector('input[type="email"]');
      if (email && !email.validity.valid) {
        event.preventDefault();
        email.focus();
      }
    });
  }
});
