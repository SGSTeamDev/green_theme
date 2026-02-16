// green_theme/public/js/green_theme.js

frappe.provide('green_theme');

// Add logo to workspace home page
frappe.ready(function() {
    // Wait for the workspace to load
    frappe.router.on('change', function() {
        if (frappe.get_route()[0] === 'Workspaces' || window.location.pathname === '/app/home' || frappe.get_route()[0] === 'desk') {
            add_logo_to_workspace();
        }
    });
    
    // Also run on initial load
    setTimeout(function() {
        if (frappe.get_route()[0] === 'Workspaces' || window.location.pathname === '/app/home' || frappe.get_route()[0] === 'desk') {
            add_logo_to_workspace();
        }
    }, 1000);
});

function add_logo_to_workspace() {
    // Check if logo already exists
    if ($('.workspace-custom-logo').length > 0) {
        return;
    }
    
    // Get the workspace container
    let workspace_container = $('.layout-main-section');
    
    if (workspace_container.length === 0) {
        workspace_container = $('#body');
    }
    
    // Get logo URL from boot or use default
    let logo_url = frappe.boot.app_logo_url || '/assets/frappe/images/frappe-framework-logo.svg';
    
    // Create logo HTML
    let logo_html = `
        <div class="workspace-custom-logo" style="text-align: center; padding: 40px 20px 30px; margin-bottom: 20px;">
            <img 
                src="${logo_url}" 
                alt="${frappe.boot.app_name || 'Logo'}"
                style="max-width: 250px; height: auto; transition: transform 0.3s ease;"
                onmouseover="this.style.transform='scale(1.05)'"
                onmouseout="this.style.transform='scale(1)'"
            />
        </div>
    `;
    
    // Prepend logo to workspace
    workspace_container.prepend(logo_html);
}

// Alternative: Add logo to the specific workspace grid container
$(document).on('app_ready', function() {
    // Override workspace rendering to include logo
    if (frappe.views && frappe.views.Workspace) {
        const original_render = frappe.views.Workspace.prototype.render;
        
        frappe.views.Workspace.prototype.render = function() {
            original_render.call(this);
            
            // Add logo after rendering
            setTimeout(() => {
                if ($('.workspace-custom-logo').length === 0) {
                    let logo_url = frappe.boot.app_logo_url || '/assets/frappe/images/frappe-framework-logo.svg';
                    
                    let logo_html = `
                        <div class="workspace-custom-logo" style="text-align: center; padding: 30px 20px 20px;">
                            <img 
                                src="${logo_url}" 
                                alt="${frappe.boot.app_name || 'Logo'}"
                                class="workspace-logo-img"
                            />
                        </div>
                    `;
                    
                    this.$wrapper.prepend(logo_html);
                }
            }, 100);
        };
    }
});