import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit (doit être au début du fichier)
st.set_page_config(page_title="Tynorah — Sign Up", layout="centered")

def main():
    # Ton code HTML/CSS/JS complet
    html_signup = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        body { margin: 0; height: 100vh; background: #f5f5f5; font-family: 'Segoe UI', sans-serif; overflow: hidden; }
        .container { 
            width: 450px; 
            max-width: 92vw; 
            background: #fff; 
            border-radius: 50px; 
            box-shadow: 0 6px 18px rgba(0,0,0,0.1); 
            position: absolute; 
            padding: 35px; 
            box-sizing: border-box; 
        }
        .header { text-align: center; margin-bottom: 20px; }
        .brand { font-weight: bold; letter-spacing: 2px; color: #333; margin-bottom: 5px; }
        h1 { margin: 0; font-size: 22px; }
        .subtitle { color: #888; font-size: 13px; }
        .row { display: flex; gap: 10px; }
        .col { flex: 1; }
        label { display: block; margin: 12px 0 5px; font-weight: 600; font-size: 12px; }
        input { width: 100%; padding: 10px; border: 1px solid #eee; border-radius: 10px; background: #f9f9f9; box-sizing: border-box; }
        .terms { display: flex; align-items: center; gap: 8px; margin-top: 15px; font-size: 12px; }
        .consent { font-size: 10px; color: #999; margin: 15px 0; text-align: center; }
        .btn { width: 100%; padding: 12px; background: #000; color: #fff; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; }
        .small { text-align: center; font-size: 12px; margin-top: 15px; color: #777; }
        .signin-link { color: #000; font-weight: bold; text-decoration: none; border-bottom: 1px solid #000; }
      </style>
    </head>
    <body>

    <div class="container">
      <header class="header">
        <div class="brand">TYNORAH</div>
        <h1>SIGN UP</h1>
        <p class="subtitle">Create your account and join the community</p>
      </header>

      <form id="signup-form">
        <div class="row">
          <div class="col">
            <label for="firstname">First name</label>
            <input id="firstname" type="text" placeholder="First name" required>
          </div>
          <div class="col">
            <label for="name">Name</label>
            <input id="name" type="text" placeholder="Name" required>
          </div>
        </div>

        <label for="email">Email</label>
        <input id="email" type="email" placeholder="example@email.com" required>

        <label for="password">Password</label>
        <input id="password" type="password" placeholder="•••••••••••••" required>

        <label for="confirm-password">Confirm password</label>
        <input id="confirm-password" type="password" placeholder="•••••••••••••" required>

        <div class="terms">
          <input id="agree" type="checkbox" required>
          <label for="agree">I agree to the terms</label>
        </div>

        <p class="consent">
          By clicking "Sign Up", you agree to our Terms of Service and Privacy Policy
        </p>

        <button class="btn" type="submit">SIGN UP</button>

        <!-- Transformation vers index.py (lien Streamlit) -->
        <p class="small">
          Already have an account? <a href="index" target="_self" class="signin-link">Sign in</a>
        </p>
      </form>
    </div>

    <script>
      function centerContainer() {
        const container = document.querySelector('.container');
        container.style.left = (window.innerWidth - container.offsetWidth) / 2 + 'px';
        container.style.top = (window.innerHeight - container.offsetHeight) / 2 + 'px';
      }

      window.addEventListener('load', centerContainer);
      window.addEventListener('resize', centerContainer);

      document.getElementById('signup-form').addEventListener('submit', function(e) {
        e.preventDefault();
        // Logique de succès (simulée)
        alert("Account created! Redirecting to login...");
        window.parent.location.assign("index"); 
      });
    </script>

    </body>
    </html>
    """

    # Affichage dans Streamlit
    # Augmente le height si le formulaire est coupé
    components.html(html_signup, height=750, scrolling=False)

if __name__ == "__main__":
    main()
