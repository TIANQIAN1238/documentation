import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import { SdkLogosAsBlocks } from './SdkLogosAsBlocks';
import '../../css/homepage-hero.css';

const Icon = ({ src, alt, className, width, height }) => {
  const darkSrc = src;
  const lightSrc = src.replace('-dark-mode-24x24.svg', '-24x24.svg');

  return (
    <>
      <img
        src={useBaseUrl(darkSrc)}
        alt={alt}
        className={`icon-dark-mode ${className || ''}`}
        width={width}
        height={height}
      />
      <img
        src={useBaseUrl(lightSrc)}
        alt={alt}
        className={`icon-light-mode ${className || ''}`}
        width={width}
        height={height}
      />
    </>
  );
};

const HomePageHero = () => {
  const actionCards = [
    {
      href: '/quickstarts',
      icon: <Icon src="/img/icons/bolt-dark-mode-24x24.svg" alt="Lightning icon" />,
      title: '快速入门',
      description: '配置本地环境并运行一个 Hello World Workflow。',
    },
    {
      href: '/develop',
      icon: <Icon src="/img/icons/code-dark-mode-24x24.svg" alt="Code icon" />,
      title: '开发指南',
      description: '深入了解构建 Temporal Workflow 所需的全部内容。',
    },
    {
      href: '/production-deployment',
      icon: <Icon src="/img/icons/rocket-dark-mode-24x24.svg" alt="Rocket icon" />,
      title: '部署 Workflow',
      description: '将 Temporal Application 部署到你的环境中。你可以 Self-Host Temporal Service，也可以使用 Temporal Cloud。',
    },
    {
      href: 'https://temporal.io/cloud',
      icon: <Icon src="/img/icons/cloud-dark-mode-24x24.svg" alt="Cloud icon" />,
      title: '免费开始，获赠 $1000 额度',
      description: '<span class="linkify">注册 Temporal Cloud</span>，让我们为你托管 Temporal Service。',
    },
  ];

  const communityCards = [
    {
      href: 'https://temporal.io/slack',
      icon: <Icon src="/img/icons/slack-dark-mode-24x24.svg" alt="Slack" />,
      title: 'Slack 社区',
      description: '加入 <a href="https://temporal.io/slack">temporal.io/slack</a>，来打个招呼或直接提问。',
    },
    {
      href: 'https://community.temporal.io',
      icon: <Icon src="/img/icons/forum-dark-mode-24x24.svg" alt="Message" />,
      title: '开发者论坛',
      description: '访问 <a href="https://community.temporal.io">开发者论坛</a>，看看你的问题是否已经有人问过。',
    },
    {
      href: 'https://learn.temporal.io/courses/',
      icon: <Icon src="/img/icons/learn-dark-mode-24x24.svg" alt="Education" />,
      title: '系统学习',
      description: '通过 <a href="https://learn.temporal.io/courses/">Temporal 官方课程</a> 学习完整知识体系。',
    },
  ];

  return (
    <div className="homepage-hero-wrapper">
      <div className="hero-main-title-container">
        <header className="hero-main-title">Temporal 文档</header>

        <div className="quickstart-links">
          <SdkLogosAsBlocks />
        </div>
      </div>

      <div className="hero-section">
        <div className="hero-content">
          <h1>构建永不失效的应用</h1>
          <p>
            Temporal 是一个用于构建可靠应用的开源平台。它通过保证应用在发生崩溃、网络故障或基础设施中断后，
            能够从中断位置准确恢复执行，从而提供具备抗崩溃能力的执行环境——无论中断发生在几秒、几天，甚至几年之后。
          </p>
          <p>
            Temporal 让开发者能够专注于交付推动业务的功能，同时确保订单履约、客户开户、支付处理等关键业务流程不会因故障而失败或丢失。
          </p>
          <a href="/quickstarts" className="hero-cta">
            快速入门
            <svg fill="none" height="18" viewBox="0 0 21 18" width="21" xmlns="http://www.w3.org/2000/svg">
              <path d="m20.1094 9.5625-7.1719 7.2187-.7969.7969-1.5937-1.5937.7969-.7969 5.25-5.29688h-15.4688-1.125v-2.25h1.125 15.4688l-5.25-5.25-.7969-.79687 1.5937-1.59375.7969.796875 7.1719 7.171875.7968.79687z" />
            </svg>
          </a>
        </div>

        <div className="hero-actions">
          {actionCards.map((card, index) => (
            <a key={index} href={card.href} className="action-card">
              <div className="action-card-inner">
                <div className="action-icon">{card.icon}</div>
                <div className="action-content">
                  <h3>{card.title}</h3>
                  <p dangerouslySetInnerHTML={{ __html: card.description }}></p>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>

      <div className="community-cards">
        {communityCards.map((card, index) => (
          <div key={index} className="community-card">
            <div className="community-icon">{card.icon}</div>
            <h3>{card.title}</h3>
            <p dangerouslySetInnerHTML={{ __html: card.description }}></p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HomePageHero;
