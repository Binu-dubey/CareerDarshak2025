
const careers = [
    {
      id: 1,
      name: "Engineering",
      image: "flat-engineering-team.avif",
      description: "Develop and maintain software applications.",
      branches: [
        { name: "Web Development", description: "Design websites and web applications." },
        { name: "Mobile Development", description: "Create mobile apps for iOS and Android." }
      ],
      responsibilities: "Design, develop, and maintain software solutions.",
      qualifications: "Bachelor’s degree in Computer Science or a related field.",
      outlook: "Growing demand in all sectors with an emphasis on automation and AI.",
      salary: "$90,000 - $150,000 annually."
    },
    {
      id: 2,
      name: "Healthcare",
      image: "/placeholder.svg",
      description: "Provide medical and health services.",
      branches: [
        { name: "Nursing", description: "Provide patient care in hospitals and clinics." },
        { name: "Pharmacy", description: "Dispense medications and offer healthcare advice." }
      ],
      responsibilities: "Assist patients with medical needs and collaborate with physicians.",
      qualifications: "Bachelor’s degree in Nursing or related medical field.",
      outlook: "High growth in aging populations and medical advancements.",
      salary: "$50,000 - $120,000 annually."
    },
    // Other careers...
  ];
  
  const careerGrid = document.getElementById("career-grid");
  const searchInput = document.getElementById("search");
  const detailCard = document.getElementById("career-detail-card");
  const careerImage = document.getElementById("career-image");
  const careerTitle = document.getElementById("career-title");
  const careerDescription = document.getElementById("career-description");
  const highlightedBranches = document.getElementById("highlighted-branches");
  const careerResponsibilities = document.getElementById("career-responsibilities");
  const careerQualifications = document.getElementById("career-qualifications");
  const careerOutlook = document.getElementById("career-outlook");
  const careerSalary = document.getElementById("career-salary");
  
  window.onload = function () {
    populateCareerGrid(careers);
  };
  
  function populateCareerGrid(careerList) {
    careerGrid.innerHTML = '';
    careerList.forEach((career) => {
      const careerCard = document.createElement("div");
      careerCard.classList.add("career-card");
      careerCard.innerHTML = `
        <img src="${career.image}" alt="${career.name}">
        <div class="card-content">
          <h3>${career.name}</h3>
          <p class="description">${career.description}</p>
        </div>
      `;
      careerCard.onmouseenter = () => showCareerDetail(career, careerCard);
      careerCard.onmouseleave = () => hideCareerDetail();
      careerGrid.appendChild(careerCard);
    });
  }
  
  function showCareerDetail(career, careerCard) {
    detailCard.classList.add("show");
    detailCard.style.top = careerCard.offsetTop + careerCard.offsetHeight + "px";
    detailCard.style.left = careerCard.offsetLeft + "px";
    
    careerImage.src = career.image;
    careerTitle.innerText = career.name;
    careerDescription.innerText = career.description;
  
    // Clear branches and populate with new ones
    highlightedBranches.innerHTML = '';
    career.branches.forEach(branch => {
      const branchDiv = document.createElement("div");
      branchDiv.innerHTML = `<strong>${branch.name}</strong>: ${branch.description}`;
      highlightedBranches.appendChild(branchDiv);
    });
  
    careerResponsibilities.innerText = career.responsibilities;
    careerQualifications.innerText = career.qualifications;
    careerOutlook.innerText = career.outlook;
    careerSalary.innerText = career.salary;
  }
  
  function hideCareerDetail() {
    detailCard.classList.remove("show");
  }
  
  function filterOptions() {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredCareers = careers.filter(career =>
      career.name.toLowerCase().includes(searchTerm)
    );
    populateCareerGrid(filteredCareers);
  }
  