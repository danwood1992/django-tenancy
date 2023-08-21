
"use client"
import Stats from '@/components/dashboard/common/stats'
import Pageheader from '@/components/dashboard/common/pageheader'
import AddPost from '@/components/dashboard/common/addpost'
import React from 'react';
import { useState } from 'react';
import { useCheckRealm } from '@/hooks/useCheckRealm';

const title = 'Dashboard'

function Dashboard() {
  const { data, loading, error } = useCheckRealm();
  // console.table(data.viewer);
  
  const [activeTab, setActiveTab] = useState('General');
  
  const myTabs = [
    { name: 'General', href: '#', current: true },
    { name: 'Timeline', href: '#', current: false },
    { name: 'Notifications', href: '#', current: false },
    { name: 'Team Members', href: '#', current: false },
    { name: 'Team Settings', href: '#', current: false },
  ];
  
  const actions = (
    <div className="page-header-actions">
      <button
        type="button"
        className="page-header-actions-button"
      >
        Share
      </button>
      <button
        type="button"
        className="ml-3 inline-flex items-center rounded-md bg-slate-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Create
      </button>
    </div>
  );

  return (
    
    <div>
      <Pageheader 
        
        title={title} 
        tabs={myTabs} 
        actions={actions} 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
      />
      {activeTab === 'General' && <div>Stats<Stats /></div>}
      {activeTab === 'Timeline' && <div>Timeline<AddPost /></div>}
      {activeTab === 'Notifications' && <div>Notifications Content</div>}
      {activeTab === 'Team Members' && <div>Team Members Content</div>}
      {activeTab === 'Team Settings' && <div>Team Settings Content</div>}
      
    </div>
  );
}

export default Dashboard;



