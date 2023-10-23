const changeThemeBtn = document.querySelector("#change-theme");

// alternar para o modo

const toggleDarkMode = () => {
    document.body.classList.toggle("dark");
}

// Carrega tema light ou dark

const loadTheme = () => {
    const darkMode = localStorage.getItem("dark");

    if(darkMode) {
        toggleDarkMode();
    }
}

loadTheme();


// Verifica qual modo o usuário tem preferência.

changeThemeBtn.addEventListener("change", () => {
    
    toggleDarkMode();
    localStorage.removeItem("dark");
    if(document.body.classList.contains("dark")) {
        localStorage.setItem("dark", 1);
    }

})



