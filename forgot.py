# forgot.py
# Module page pour la réinitialisation. Expose show().

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
      <title>Tynorah — Reset Password</title>
      <style>
        html,body{height:100%;margin:0;font-family:Inter,system-ui,Arial;}
        body{background:#f5f5f5;position:relative;min-height:100vh;}
        .container{width:450px;max-width:92vw;background:#fff;border-radius:50px;box-shadow:0 6px 18px rgba(0,0,0,0.1);position:absolute;padding:20px;box-sizing:border-box;}
        .header{text-align:center;margin-bottom:12px;}
        .brand{font-weight:800;letter-spacing:4px;color:#111827;margin-bottom:6px;}
        h1{margin:0;font-size:28px;font-weight:800;}
        .subtitle{color:#6b7280;margin-top:6px;font-size:14px;}
        label{display:block;margin-top:12px;font-weight:700;font-size:13px;color:#111827;}
        input[type="email"]{width:100%;padding:12px;border-radius:8px;border:1.5px solid #e6e6eb;background:#fafafa;margin-top:6px;box-sizing:border-box;}
        .btn{margin-top:20px;padding:12px;border-radius:10px;border:none;background:linear-gradient(90deg,#7800F6,#1465FF);color:#fff;font-weight:800;cursor:pointer;width:100%;}
        .small{text-align:center;margin-top:14px;color:#6b7280;font-size:13px;}
      </style>
    </head>
    <body>
    <div class="container" id="forgot-container">
      <header class="header">
        <div class="brand">TYNORAH</div>
        <h1>RESET PASSWORD</h1>
        <p class="subtitle">Enter your email to receive a reset link</p>
      </header>

      <form id="forgot-form" onsubmit="return handleSubmit(event);">
        <div style="margin-top:20px;">
          <label for="reset-email">Email Address</label>
          <input id="reset-email" type="email" placeholder="example@email.com" required>
        </div>

        <p class="consent" style="text-align:left;margin-top:15px;">
          We will send you a secure link to update your password. Please check your spam folder if you don't see it.
        </p>

        <button class="btn" type="submit">SEND RESET LINK</button>

        <p class="small">
          Wait, I remember it! <a href="?page=signin" target="_top" class="signin-link">Back to login</a>
        </p>
      </form>
    </div>

    <script>
      function centerContainer() {
        const c = document.getElementById('forgot-container');
        if(!c) return;
        const left = Math.max((window.innerWidth - c.offsetWidth)/2, 12);
        const top = Math.max((window.innerHeight - c.offsetHeight)/2, 12);
        c.style.left = left + 'px';
        c.style.top = top + 'px';
      }
      window.addEventListener('load', centerContainer);
      window.addEventListener('resize', centerContainer);

      function handleSubmit(e) {
        e.preventDefault();
        const email = document.getElementById('reset-email').value.trim();
        if (!email) {
          alert("Veuillez entrer une adresse email valide.");
          return false;
        }
        alert("Si un compte est associé à " + email + ", un lien de réinitialisation sera envoyé.");
        try {
          window.top.location.search = '?page=signin';
        } catch (err) {
          window.location.search = '?page=signin';
        }
        return false;
      }
    </script>
    </body>
    </html>
    """

    components.html(html, height=800, scrolling=True)
