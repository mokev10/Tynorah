import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit
st.set_page_config(page_title="Tynorah — Sign In", layout="centered")

def main():
    # TON CODE HTML SOURCE - NON MODIFIÉ
    html_code = """
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
      <!-- Correction technique pour Streamlit : .html retiré et target="_parent" ajouté -->
      <a href="forgot-password" target="_parent" class="signin-link" style="font-size: 11px;">Forgot password?</a>
    </div>
    <input id="login-password" name="password" type="password" autocomplete="current-password" placeholder="•••••••••••••" required>

    <div class="terms">
      <input id="remember" type="checkbox">
      <label for="remember" class="terms-label">Remember me</label>
    </div>

    <button class="btn" type="submit" style="margin-top: 30px;">SIGN IN</button>

    <p class="small">
      Don't have an account? 
      <!-- Correction technique pour Streamlit : .html remplacé par /signup et target="_parent" ajouté -->
      <a href="/signup" target="_parent" class="signin-link">Sign up</a>
    </p>
  </form>
</div>

<script>
  // Fonction pour centrer le container
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

  // Gestion du formulaire
  document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault(); // empêche l'envoi réel

    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value.trim();

    // Redirection vers feed (Streamlit) si "authentification" réussie
    if (email !== "" && password !== "") {
      window.parent.location.assign("/feed");
    } else {
      alert("Veuillez entrer vos identifiants.");
    }
  });
</script>

</body>
</html>
"""

    # Rendu du composant
    components.html(html_code, height=850, scrolling=False)

if __name__ == "__main__":
    main()
