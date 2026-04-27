import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Tynorah — Sign In", layout="centered")

def main():
    # TON CODE ORIGINAL STRICT (AUCUNE SIMPLIFICATION)
    html_index = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tynorah — Sign In</title>
  <link rel="stylesheet" href="style.css">
  <style>
    body {
      margin: 0;
      height: 100vh;
      background: #f5f5f5;
      position: relative;
    }
    .container {
      width: 450px;
      max-width: 92vw;
      background: #fff;
      border-radius: 60px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.1);
      position: absolute; /* nécessaire pour JS */
      padding: 20px;
    }
    /* Ajout du CSS pour que le rendu soit identique à ton image */
    .header { text-align: center; margin-bottom: 20px; }
    .brand { font-weight: bold; letter-spacing: 2px; color: #333; margin-bottom: 5px; }
    h1 { margin: 0; font-size: 24px; }
    .subtitle { color: #888; font-size: 14px; margin-top: 5px; }
    label { display: block; margin: 15px 0 5px; font-weight: 600; font-size: 13px; }
    input { width: 100%; padding: 12px; border: 1px solid #eee; border-radius: 10px; background: #f9f9f9; box-sizing: border-box; outline: none; }
    .btn { width: 100%; padding: 14px; background: #000; color: #fff; border: none; border-radius: 30px; cursor: pointer; font-weight: bold; margin-top: 30px; }
    .small { text-align: center; font-size: 12px; margin-top: 20px; color: #777; }
    .signin-link { color: #000; font-weight: bold; text-decoration: none; border-bottom: 1px solid #000; }
  </style>
</head>
<body>

<div class="container">
  <header class="header">
    <div class="brand">TYNORAH</div>
    <h1>LOGIN</h1>
    <p class="subtitle">Enter your details to access your account</p>
  </header>

  <form id="login-form" class="content" action="#" method="POST">
    <label for="login-email">Email</label>
    <input id="login-email" name="email" type="email" autocomplete="username" placeholder="example@email.com" required>

    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
      <label for="login-password">Password</label>
      <a href="forgot-password" target="_parent" class="signin-link" style="font-size: 11px;">Forgot password?</a>
    </div>
    <input id="login-password" name="password" type="password" autocomplete="current-password" placeholder="•••••••••••••" required>

    <div class="terms">
      <input id="remember" type="checkbox">
      <label for="remember" class="terms-label">Remember me</label>
    </div>

    <button class="btn" type="submit" style="margin-top: 30px;">SIGN IN</button>

    <p class="small">
      Don't have an account? <a href="/signup" target="_parent" class="signin-link">Sign up</a>
    </p>
  </form>
</div>

<script>
  // Fonction pour centrer le container (TON CODE ORIGINAL)
  function centerContainer() {
    const container = document.querySelector('.container');
    const winWidth = window.innerWidth;
    const winHeight = window.innerHeight;
    const contWidth = container.offsetWidth;
    const contHeight = container.offsetHeight;

    const left = (winWidth - contWidth) / 2;
    const top = (winHeight - contHeight) / 2;

    container.style.left = left + 'px';
    container.style.top = top + 'px';
  }

  window.addEventListener('load', centerContainer);
  window.addEventListener('resize', centerContainer);

  // Gestion du formulaire (TON CODE ORIGINAL)
  document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault(); 

    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value.trim();

    if (email !== "" && password !== "") {
      // Pour Streamlit, on utilise parent pour sortir de l'iframe
      window.parent.location.assign("/feed");
    } else {
      alert("Veuillez entrer vos identifiants.");
    }
  });
</script>

</body>
</html>"""

    # Affichage du composant
    components.html(html_index, height=800, scrolling=False)

if __name__ == "__main__":
    main()
