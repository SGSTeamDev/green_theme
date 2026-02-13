frappe.router.on('change', () => {
    if (frappe.get_route()[0] === 'Workspaces') {
        // Wait briefly for the workspace to render
        setTimeout(() => {
            add_custom_logo();
        }, 500);
    }
});

function add_custom_logo() {
    // Prevent duplicate logos if the user navigates back and forth
    if (document.querySelector('.custom-workspace-logo')) return;

    const workspace_container = document.querySelector('.page-container');
    if (workspace_container) {
        const logo_div = document.createElement('div');
        logo_div.className = 'custom-workspace-logo';
        logo_div.innerHTML = `
            <img src="/assets/green_theme/images/your-logo.png" 
                 style="max-width: 200px; margin: 20px auto; display: block; opacity: 0.8;">
        `;
        
        // Prepends the logo to the top of the workspace content
        workspace_container.prepend(logo_div);
    }
}