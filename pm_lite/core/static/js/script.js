// Simple client-side filter + search for tasks on project_detail
(function () {
  const list = document.getElementById('taskList');
  if (!list) return;

  const statusSelect = document.getElementById('statusFilter');
  const searchInput = document.getElementById('taskSearch');

  const applyFilters = () => {
    const status = (statusSelect?.value || '').toUpperCase();
    const q = (searchInput?.value || '').trim().toLowerCase();

    list.querySelectorAll('.task-item').forEach(li => {
      const matchesStatus = !status || li.dataset.status === status;
      const matchesText = !q || (li.dataset.title || '').includes(q);
      li.style.display = (matchesStatus && matchesText) ? '' : 'none';
    });
  };

  statusSelect?.addEventListener('change', applyFilters);
  searchInput?.addEventListener('input', applyFilters);
})();
