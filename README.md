# LENEHRT static portfolio

This is a static recreation of Leonardo De Oliveira's portfolio, based on a WPvivid backup dated February 4, 2025. It contains HTML, CSS, a small menu script, and locally stored images. It does not require WordPress, PHP, a database, a build command, or third party CSS/JS.

## Preview locally

From this folder, run `python3 -m http.server 8000`, then open `http://localhost:8000`.

## Publish with GitHub Pages

1. Create a GitHub repository and upload **the contents of this folder** to its root. `index.html` must be at the repository root.
2. In the repository, open **Settings → Pages** and select **Deploy from a branch**. Choose the `main` branch and `/ (root)`, then save.
3. GitHub will show the Pages URL when deployment completes. The site also works under a project path such as `username.github.io/repository-name/` because all internal URLs are relative.
4. If you plan to use `lenehrt.com`, add the domain in the Pages settings and update DNS using GitHub's current instructions. Test the Pages URL before switching DNS.

## Update content

- Home page: `index.html`
- Projects list: `projects/index.html`
- Individual writeups: each project's `index.html`
- Contact address and résumé link appear in multiple HTML pages. Search for `leonardo@lenehrt.com` and the current Google Drive URL to update them everywhere.
- Shared styling and menu behavior: `assets/style.css` and `assets/site.js`

The project writeups and résumé link came from the 2025 backup. Review the dates, employer wording, education, links, and articles before publishing. The former Elementor contact form was replaced with an email link. The privacy page describes this static version; it is separate from the old WordPress policy.
