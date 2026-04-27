# signup.py
# Module page pour l'inscription. Expose une fonction show() appelée par index.py
# Le HTML embarqué utilise des liens vers ?page=signin et ?page=feed pour naviguer via le routeur.

import streamlit as st
import streamlit.components.v1 as components

def show():
    st.markdown("<style>.stApp { min-height: 100vh; }</style>", unsafe_allow_html=True)

    html = """
    <!doctype html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Tynorah — Sign Up</title>
      <style>
        html,body{height:100%;margin:0;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;}
        body{background:#f5f5f5;position:relative;min-height:100vh;}
        .container{width:450px;max-width:92vw;background:#fff;border-radius:50px;box-shadow:0 6px 18px rgba(0,0,0,0.1);position:absolute;padding:20px;box-sizing:border-box;}
        .header{text-align:center;margin-bottom:12px;}
        .brand{font-weight:800;letter-spacing:4px;color:#111827;margin-bottom:6px;}
        h1{margin:0;font-size:28px;font-weight:800;}
        .subtitle{color:#6b7280;margin-top:6px;font-size:14px;}
        .row{display:flex;gap:12px;margin-top:10px;}
        .col{flex:1;}
        label{display:block;margin-top:12px;font-weight:700;font-size:13px;color:#111827;}
        input[type="email"], input[type="password"], input[type="text"]{
          width:100%;padding:12px;border-radius:8px;border:1.5px solid #e6e6eb;background:#fafafa;margin-top:6px;box-sizing:border-box;
        }
        .terms{display:flex;align-items:center;gap:10px;margin-top:12px;}
        .btn{margin-top:12px;padding:12px;border-radius:10px;border:none;background:linear-gradient(90deg,#7800F6,#1465FF);color:#fff;font-weight:800;cursor:pointer;width:100%;}
        .small{text-align:center;margin-top:14px;color:#6b7280;font-size:13px;}
        .signin-link{color:#6b46ff;text-decoration:none;font-weight:700;}
        #error-message{color:red;margin-bottom:10px;}
      </style>
    </head>
    <body>

    <div class="container" id="signup-container">
      <header class="header">
        <div class="brand">TYNORAH</div>
        <h1>SIGN UP</h1>
        <p class="subtitle">Create your account and join the community</p>
      </header>

      <form id="signup-form" class="content" action="#" method="POST" onsubmit="return handleSubmit(event);">
        <div class="row">
          <div class="col">
            <label for="firstname">First name</label>
            <input id="firstname" name="firstname" type="text" placeholder="First name" required>
          </div>
          <div class="col">
            <label for="name">Name</label>
            <input id="name" name="name" type="text" placeholder="Name" required>
          </div>
        </div>

        <label for="email">Email</label>
        <input id="email" name="email" type="email" placeholder="example@email.com" required>

        <label for="password">Password</label>
        <input id="password" name="password" type="password" placeholder="•••••••••••••" required>

        <label for="confirm-password">Confirm password</label>
        <input id="confirm-password" name="confirm-password" type="password" placeholder="•••••••••••••" required>

        <div id="error-message"></div>

        <div class="terms">
          <input id="agree" name="agree" type="checkbox" required>
          <label for="agree" class="terms-label">I agree to the terms</label>
        </div>

        <p class="consent" style="margin-top:10px;">
          By clicking "Sign Up", you agree to our Terms of Service and Privacy Policy
        </p>

        <button class="btn" type="submit">SIGN UP</button>

        <p class="small">
          Already have an account? <a href="?page=signin" class="signin-link">Sign in</a>
        </p>
      </form>
    </div>

    <script>
      // Centrage du container
      function centerContainer() {
        const container = document.getElementById('signup-container');
        if (!container) return;
        const left = Math.max((window.innerWidth - container.offsetWidth) / 2, 12);
        const top = Math.max((window.innerHeight - container.offsetHeight) / 2, 12);
        container.style.left = left + 'px';
        container.style.top = top + 'px';
      }
      window.addEventListener('load', centerContainer);
      window.addEventListener('resize', centerContainer);

      // Validation simple côté client puis navigation via query param
      function handleSubmit(e) {
        e.preventDefault();
        const firstname = document.getElementById('firstname').value.trim();
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        const confirm = document.getElementById('confirm-password').value;
        const agree = document.getElementById('agree').checked;
        const err = document.getElementById('error-message');
        err.textContent = '';

        if (!firstname || !name || !email || !password || !confirm) {
          err.textContent = 'Veuillez remplir tous les champs.';
          return false;
        }
        if (password !== confirm) {
          err.textContent = 'Les mots de passe ne correspondent pas.';
          return false;
        }
        if (!agree) {
          err.textContent = 'Vous devez accepter les conditions.';
          return false;
        }

        // Simuler succès -> naviguer vers feed via query param
        window.location.search = '?page=feed';
        return false;
      }
    </script>

    </body>
    </html>
    """

    components.html(html, height=900, scrolling=True)
