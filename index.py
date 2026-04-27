# index.py
# Streamlit wrapper that embeds the original sign-in HTML (converted to use .py links)
# The HTML includes a small JS routine to center the .container and to redirect on submit.
# Usage: streamlit run index.py

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="TYNORA SIGN IN",
    page_icon="https://img.icons8.com/ios-filled/50/t-key.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
html = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tynorah — Sign In</title>
  <style>
    /* Minimal reset + styles (kept inline so the component is self-contained) */
    html,body{height:100%;margin:0;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;}
    body{background:#f5f5f5;position:relative;min-height:100vh;}
    .container{
      width:450px;
      max-width:92vw;
      background:#fff;
      border-radius:60px;
      box-shadow:0 6px 18px rgba(0,0,0,0.1);
      position:absolute;
      padding:20px;
      box-sizing:border-box;
    }
    .header{text-align:center;margin-bottom:12px;}
    .brand{font-weight:800;letter-spacing:4px;color:#111827;margin-bottom:6px;}
    h1{margin:0;font-size:28px;font-weight:800;}
    .subtitle{color:#6b7280;margin-top:6px;font-size:14px;}
    label{display:block;margin-top:12px;font-weight:700;font-size:13px;color:#111827;}
    input[type="email"], input[type="password"], input[type="text"]{
      width:100%;padding:12px;border-radius:8px;border:1.5px solid #e6e6eb;background:#fafafa;margin-top:6px;box-sizing:border-box;
    }
    .terms{display:flex;align-items:center;gap:10px;margin-top:12px;}
    .btn{margin-top:30px;padding:12px;border-radius:10px;border:none;background:linear-gradient(90deg,#7800F6,#1465FF);color:#fff;font-weight:800;cursor:pointer;width:100%;}
    .small{text-align:center;margin-top:14px;color:#6b7280;font-size:13px;}
    .signin-link{color:#6b46ff;text-decoration:none;font-weight:700;}
    a.signin-link-small{font-size:11px;color:#6b46ff;text-decoration:none;}
  </style>
</head>
<body>

<div class="container" id="auth-container">
  <header class="header">
    <div class="brand">TYNORAH</div>
    <h1>LOGIN</h1>
    <p class="subtitle">Enter your details to access your account</p>
  </header>

  <form id="login-form" class="content" action="#" method="POST" onsubmit="return handleSubmit(event);">
    <label for="login-email">Email</label>
    <input id="login-email" name="email" type="email" autocomplete="username" placeholder="example@email.com" required>

    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
      <label for="login-password">Password</label>
      <a href="forgot-password.py" class="signin-link-small">Forgot password?</a>
    </div>
    <input id="login-password" name="password" type="password" autocomplete="current-password" placeholder="•••••••••••••" required>

    <div class="terms">
      <input id="remember" type="checkbox">
      <label for="remember" class="terms-label">Remember me</label>
    </div>

    <button class="btn" type="submit">SIGN IN</button>

    <p class="small">
      Don't have an account? <a href="signup.py" class="signin-link">Sign up</a>
    </p>
  </form>
</div>

<script>
  // Centering function: positions the .container in the middle of the viewport
  function centerContainer() {
    const container = document.getElementById('auth-container');
    if (!container) return;
    const winWidth = window.innerWidth;
    const winHeight = window.innerHeight;
    const contWidth = container.offsetWidth;
    const contHeight = container.offsetHeight;

    const left = Math.max((winWidth - contWidth) / 2, 12); // keep a small margin on very small screens
    const top = Math.max((winHeight - contHeight) / 2, 12);

    container.style.left = left + 'px';
    container.style.top = top + 'px';
  }

  // Call on load and resize
  window.addEventListener('load', centerContainer);
  window.addEventListener('resize', centerContainer);

  // Handle form submit: simple client-side check then redirect to feed.py
  function handleSubmit(e) {
    e.preventDefault();
    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value.trim();

    if (email === "" || password === "") {
      alert("Veuillez entrer vos identifiants.");
      return false;
    }

    // Simulated authentication success -> redirect to feed.py
    // In a real app, replace with an API call and server-side validation.
    window.location.href = "feed.py";
    return false;
  }
</script>

</body>
</html>
"""

# Embed the HTML in a Streamlit component so the JS runs inside the page
# Height is set to window innerHeight via a small trick: set a large height and allow scrolling.
components.html(html, height=900, scrolling=True)

# Note for developer: when you create the other pages, name them signup.py, forgot-password.py, feed.py
# and follow the same pattern (embed HTML or use Streamlit native widgets).
