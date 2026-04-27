import streamlit as st
import streamlit.components.v1 as components

def main():
    # Configuration de la page
    st.set_page_config(page_title="Tynorah — Sign In", layout="centered")

    # Contenu HTML de la page de connexion
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
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        .container {
          width: 450px;
          max-width: 92vw;
          background: #fff;
          border-radius: 40px;
          box-shadow: 0 6px 18px rgba(0,0,0,0.1);
          padding: 40px;
          box-sizing: border-box;
        }
        .header { text-align: center; margin-bottom: 30px; }
        .brand { font-weight: bold; letter-spacing: 2px; color: #333; margin-bottom: 5px; }
        h1 { margin: 0; font-size: 22px; text-transform: uppercase; }
        .subtitle { color: #888; font-size: 13px; margin-top: 5px; }
        
        label { display: block; margin: 15px 0 5px; font-weight: 600; font-size: 12px; color: #444; }
        input {
          width: 100%;
          padding: 12px;
          border: 1px solid #eee;
          border-radius: 10px;
          background: #f9f9f9;
          box-sizing: border-box;
          outline: none;
        }
        .btn {
          width: 100%;
          padding: 14px;
          background: #000;
          color: #fff;
          border: none;
          border-radius: 30px;
          cursor: pointer;
          font-weight: bold;
          margin-top: 25px;
        }
        
        .small { text-align: center; font-size: 12px; margin-top: 20px; color: #777; }
        .signin-link { 
            color: #000; 
            font-weight: bold; 
            text-decoration: none; 
            border-bottom: 1px solid #000;
            cursor: pointer;
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

      <form id="login-form">
        <label>Email</label>
        <input type="email" placeholder="example@email.com" required>

        <label>Password</label>
        <input type="password" placeholder="•••••••••••••" required>

        <button class="btn" type="submit">SIGN IN</button>

        <p class="small">
          Don't have an account? <a href="/signup" target="_parent" class="signin-link">Sign up</a>
        </p>
      </form>
    </div>

    <script>
      document.getElementById('login-form').addEventListener('submit', function(e) {
        e.preventDefault();
        alert("Login successful!");
      });
    </script>

    </body>
    </html>
    """

    # Affichage du HTML
    components.html(html_content, height=600)

if __name__ == "__main__":
    main()
