// Load the Botpress Injection Script
function loadBotpress() {
    const script1 = document.createElement('script');
    script1.src = "https://cdn.botpress.cloud/webchat/v3.6/inject.js";
    script1.defer = true;
    
    script1.onload = () => {
        const script2 = document.createElement('script');
        script2.src = "https://files.bpcontent.cloud/2026/02/09/20/20260209204543-XW9JCDPP.js";
        script2.defer = true;
        document.body.appendChild(script2);
    };

    document.body.appendChild(script1);
}

// Initialize when the desk is ready
$(document).ready(() => {
    loadBotpress();
});