// Replace Text on Login Form
const checkReplace = document.querySelector('.replace-me');

if (checkReplace != null) {
  const replace = new ReplaceMe(checkReplace, {
    animation: 'animated fadeIn',
    speed: 1500,
    separator: ',',
    loopCount: 'infinite',
    autoRun: true,
  });
}
