document.addEventListener('DOMContentLoaded', () => {
  // Аккордеон
  const tableTitle = document.querySelectorAll('.table-title');
  const tableTitleTxt = document.querySelectorAll('.table-title > div');
  const tableIcon = document.querySelectorAll('.table-icon');
  const tableDesc = document.querySelectorAll('.table-desc');

  for (let i = 0; i < tableTitle.length; i++) {
    tableTitle[i].addEventListener('click', function () {
      tableIcon[i].classList.toggle('table-icon-rotate');
      const panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
        tableTitle[i].style.backgroundColor = null;
        tableTitleTxt[i].style.color = '#15A2DE';
        tableDesc[i].style.borderBottom = 'none';
      } else {
        panel.style.maxHeight = panel.scrollHeight + 'px';
        tableTitle[i].style.backgroundColor = '#15A2DE';
        tableTitleTxt[i].style.color = '#FFFFFF';
        tableDesc[i].style.borderBottom = '1px solid #15A2DE';
      }
    });
  }

  // Modal
  const modal = document.querySelector('.modal');
  const modalOverlay = document.querySelector('.modal-overlay');
  const modalCancelBtn = document.querySelector('.modal-window-cancel');
  const introBtn = document.querySelector('.intro-btn > a');

  introBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.add('modal-show');
  });

  modalCancelBtn.addEventListener('click', () => {
    modal.classList.remove('modal-show');
  });

  modalOverlay.addEventListener('mousedown', (e) => {
    if (e.target == modalOverlay) {
      modal.classList.remove('modal-show');
    }
  });

  // Modal
  const fadeIn = (el, timeout, display) => {
    el.style.opacity = 0;
    el.style.display = display || 'block';
    el.style.transition = `opacity ${timeout}ms`;
    setTimeout(() => {
      el.style.opacity = 1;
    }, 10);
  };

  const fadeOut = (el, timeout) => {
    el.style.opacity = 1;
    el.style.transition = `opacity ${timeout}ms`;
    el.style.opacity = 0;
    setTimeout(() => {
      el.style.display = 'none';
    }, timeout);
  };

  const block = document.querySelector('.block');
  const btn = document.querySelector('.btn');

  let flag = false;

  btn.addEventListener('click', (e) => {
    if (!flag) {
      fadeIn(block, 300, 'flex');
      flag = true;
    } else {
      fadeOut(block, 300);
      flag = false;
    }
  });
});
