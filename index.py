import streamlit as st
import streamlit.components.v1 as components

def main():
    # Configuration de la page
    st.set_page_config(page_title="Tynorah Login", layout="centered")

    # Ton code HTML (nettoyé des guillemets inutiles au milieu des strings)
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        body {
          margin: 0;
          height: 100vh;
          background: #f5f5f5;
          font-family: sans-serif;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        .container {
          width: 450px;
          max-width: 90vw;
          background: #fff;
          border-radius: 40px;
          box-shadow: 0 6px 18px rgba(0,0,0,0.1);
          padding: 40px;
          text-align: center;
        }
        .brand { font-weight: bold; letter-spacing: 2px; color: #333; margin-bottom: 10px; }
        h1 { margin: 0; font-size: 24px; }
        .subtitle { color: #666; font-size: 14px; margin-bottom: 30px; }
        form { text-align: left; }
        label { display: block; margin-bottom: 5px; font-weight: bold; font-size: 13px; }
        input[type="email"], input[type="password"] {
          width: 100%;
          padding: 12px;
          margin-bottom: 20px;
          border: 1px solid #ddd;
          border-radius: 8px;
          box-sizing: border-box;
        }
        .btn {
          width: 100%;
          padding: 12px;
          background: #000;
          color: #fff;
          border: none;
          border-radius: 25px;
          cursor: pointer;
          font-weight: bold;
        }
        .small { font-size: 12px; margin-top: 20px; color: #666; }
        .signin-link { color: #007bff; text-decoration: none; }
      </style>
    </head>
    <body>

    <div class="container">
      <header class="header">
        <div class="brand">TYNORAH</div>
        <h1>LOGIN</h1>
        <p class="subtitle">Enter your details to access your account</p>
      </header>

      <form id="login-form">
        <label for="login-email">Email</label>
        <input id="login-email" type="email" placeholder="example@email.com" required>

        <div style="display: flex; justify-content: space-between;">
          <label>Password</label>
          <a href="#" class="signin-link" style="font-size: 11px;">Forgot password?</a>
        </div>
        <input id="login-password" type="password" placeholder="•••••••••••••" required>

        <button class="btn" type="submit">SIGN IN</button>

        <p class="small">
          Don't have an account? <a href="#" class="signin-link">Sign up</a>
        </p>
      </form>
    </div>

    <script>
      document.getElementById('login-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('login-email').value;
        alert("Tentative de connexion pour : " + email);
        // Note: window.location.href ne fonctionnera que si le fichier existe
      });
    </script>
    </body>
    </html>
    """

    # Affichage du composant HTML dans Streamlit
    components.html(html_content, height=600, scrolling=False)

if __name__ == "__main__":
    main()
