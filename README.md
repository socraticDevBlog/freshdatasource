# freshdatasource

## our cloud infrastructure ☁️

here are the various ways host our products and how we automate our deployments to production

### main website : freshdatasource.com

[freshdatasource.com](freshdatasource.com) domain name belongs to @socraticdevblog.

we use a small virtual private server. Its public ip address is mapped to domain `freshdatasource.com`.

#### CI/CD ⚙️

our continuous integration and deployment strategy is based aroun `ssh` tunneling to our vps. we use [Appleboy SSH for GitHub Actions](https://github.com/appleboy/ssh-action) to transfer (`SCP`) files from repository to server and basic bash commands from ssh to move assets to our `nginx` web server's public folder.

in order to keep everything tidy, we had set up specific `user`, `group`, and `permissions` on the server to allow continuous deployment of web assets from this repo `GitHub Actions pipeline`:

1. Read/Write permission to `nginx` web directory is given to group: `web-data`
2. A specific user dedicated to CI jobs has been created and assigned to the `web-data` group
3. This CI-user was given its own `ssh` keys
   1. its public key was written to the `~/.ssh/authorized_keys` file
   2. its private key was assigned to this repository GitHub secret `SSHKEY`
4. Following Appleboy's documentation, we have also created GitHub secrets for these variables:
   1. `HOST`: freshdatasource.com
   2. `PORT`: 22
   3. `USERNAME`: _our CI-dedicated linux user's username_

### Wall art dedicated website: https://quebec-art.freshdatasource.com

'OPEN AIR ART GALLERY: hand-picked graffiti and wall art from Quebec City, Canada' is a website dedicated to Quebec City's graffiti and wall art. it is based on an html template freely provided by [https://templatemo.com](https://templatemo.com). it uses a different code repository than this one : [https://github.com/socraticDevBlog/quebecy-city-wall-art](https://github.com/socraticDevBlog/quebecy-city-wall-art).

#### Infrastructure and CI/CD ⚙️

This website is hosted on [https://www.netlify.com](https://www.netlify.com) CDN. Since we expect a worldwide interest, we picked an affordable (free) distributed infrastructre which provide quick access to our content no matter where our visitors are located.

`netflify` provides its own CICD solution. it starts from a webhook triggered by any pushes to main branch in our repository. it basically transfers our web assets to its `CDN`. and it also can build any website that would require to get built via `npm` or `yarn`.