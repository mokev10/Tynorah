import streamlit as st
import streamlit.components.v1 as components

def signup_page():
    # Configuration de la page Streamlit
    st.set_page_config(page_title="Tynorah — Sign Up", layout="centered")

    # Contenu HTML/CSS
    # Les liens href="index.html" sont devenus href="index" (ou le nom de votre fichier page)
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
          transition: 0.3s;
        }
        .btn:hover { background: #333; }
        
        .small { text-align: center; font-size: 12px; margin-top: 20px; color: #777; }
        .signin-link { 
            color: #000; 
            font-weight: bold; 
            text-decoration: none; 
            border-bottom: 1px solid #000;
        }
      </style>
    </head>
    <body>

    <div class="container">
      <header class="header">
        <div class="brand">TYNORAH</div>
        <h1>CREATE ACCOUNT</h1>
        <p class="subtitle">Join us to start your journey</p>
      </header>

      <form id="signup-form">
        <label>Full Name</label>
        <input type="text" placeholder="John Doe" required>

        <label>Email</label>
        <input type="email" placeholder="example@email.com" required>

        <label>Password</label>
        <input type="password" placeholder="•••••••••••••" required>

        <button class="btn" type="submit">SIGN UP</button>

        <!-- Transformation demandée : index.html -> index.py -->
        <p class="small">
          Already have an account? <a href="index" target="_self" class="signin-link">Sign in</a>
        </p>
      </form>
    </div>

    <script>
      document.getElementById('signup-form').addEventListener('submit', function(e) {
        e.preventDefault();
        alert("Account created successfully!");
        // Redirection vers index.py après succès
        window.parent.location.assign("index"); 
      });
    </script>

    </body>
    </html>
    """

    # Affichage
    components.html(html_content, height=700)

if __name__ == "__main__":
    signup_page()
