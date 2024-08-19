if (document.getElementById('my-work-link')) {
  document.getElementById('my-work-link').addEventListener('click', () => {
    document.getElementById('my-work-section').scrollIntoView({behavior: "smooth"})
  })
}

if (document.getElementById('my-research-link')) {
  document.getElementById('my-research-link').addEventListener('click', () => {
    document.getElementById('my-research-section').scrollIntoView({behavior: "smooth"})
  })
}

if (document.getElementById('my-project-link')) {
  document.getElementById('my-project-link').addEventListener('click', () => {
    document.getElementById('my-project-section').scrollIntoView({behavior: "smooth"})
  })
}