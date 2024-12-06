function validatePasswords() {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    if (password !== confirmPassword) {
        alert("As senhas não combinam! Tente de novo 😒");
        return false; // Impede o envio do formulário
    }

    return true; // Permite o envio do formulário
}
